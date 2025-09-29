#!/usr/bin/env python3
import http.server
import socketserver
import os
import socket
from urllib.parse import urlparse, unquote
from pathlib import Path

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Disable caching to ensure updates are visible
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        # Parse the URL path
        parsed_path = urlparse(self.path)
        path = unquote(parsed_path.path)
        
        # Remove leading slash for file system access
        if path.startswith('/'):
            path = path[1:]
        
        # If empty path, serve the main site
        if not path or path == '/':
            path = 'dear-jean.co.za/index.html'
        
        # Check if path exists as-is
        if os.path.exists(path):
            self.path = '/' + path
            return super().do_GET()
        
        # If requesting a directory without trailing slash, try index.html
        if os.path.isdir(path):
            index_path = os.path.join(path, 'index.html')
            if os.path.exists(index_path):
                self.path = '/' + index_path
                return super().do_GET()
        
        # Try adding .html extension
        html_path = path + '.html'
        if os.path.exists(html_path):
            self.path = '/' + html_path
            return super().do_GET()
        
        # Default handling
        return super().do_GET()

class ReusableTCPServer(socketserver.TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)

def run_server():
    PORT = 5000
    HOST = "0.0.0.0"
    
    with ReusableTCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Server running at http://{HOST}:{PORT}")
        print(f"Serving Dear Jean website from current directory")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    run_server()