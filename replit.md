# Dear Jean - Luxury Sea Point Apartments Website

## Project Overview
This is a static website for Dear Jean, a luxury apartment development in Sea Point, South Africa. The site showcases high-end apartment offerings with modern design and stunning ocean views.

**Project Status**: Fully functional and deployed
**Technology**: Static HTML/CSS/JS site (originally WordPress, exported via HTTrack)
**Server**: Custom Python HTTP server on port 5000

## Project Structure
```
/
├── server.py                 # Custom Python HTTP server
├── dear-jean.co.za/         # Main website content
│   ├── index.html           # Homepage
│   ├── wp-content/          # WordPress assets (CSS, JS, images)
│   │   ├── themes/salient/  # Salient theme files
│   │   ├── plugins/         # WordPress plugin assets
│   │   └── uploads/2025/09/ # Images and media files
│   ├── bond-originators/    # Bond originators page
│   ├── faqs/               # FAQ page
│   └── privacy-policy/     # Privacy policy page
├── www.google.com/         # External Google services cache
├── www.googletagmanager.com/ # Google Tag Manager cache
└── hts-cache/              # HTTrack cache files
```

## Setup and Configuration

### Development Server
- **Port**: 5000 (required for Replit environment)
- **Host**: 0.0.0.0 (allows external access)
- **Cache Control**: Disabled for development
- **Asset Routing**: Custom logic to serve WordPress assets from `dear-jean.co.za/` directory

### Key Features of Custom Server
- Serves main site from `dear-jean.co.za/index.html` on root path
- Automatically routes asset requests to proper WordPress directory structure  
- Handles CSS, JS, images, and other static assets
- Cache headers disabled to ensure fresh content during development

### Deployment Configuration
- **Type**: Autoscale (stateless static site)
- **Command**: `python server.py`
- **Environment**: Production-ready Python HTTP server

## Site Features
- **Responsive Design**: Mobile-friendly layout
- **Modern UI**: Salient WordPress theme with custom styling
- **Media Rich**: High-quality apartment images and videos
- **Contact Forms**: Contact Form 7 integration
- **Analytics**: Google Analytics and Tag Manager
- **Cookie Consent**: GDPR compliance features

## Technical Notes
- Original WordPress site exported using HTTrack Website Copier
- All dynamic PHP functionality converted to static files
- Asset paths adjusted for static serving
- External services (Google fonts, reCAPTCHA) still functional
- Some WordPress admin features and dynamic elements are non-functional (expected for static export)

## Recent Changes
- **2025-09-29**: Initial Replit setup and server configuration
- Custom Python server implemented for proper asset routing
- All WordPress assets successfully serving with correct MIME types
- Deployment configuration set to autoscale for production use

## User Preferences
- Static site deployment preferred over dynamic WordPress hosting
- Focus on visual fidelity and fast loading times
- Minimal maintenance approach for production use

## Architecture Decisions
- **Custom HTTP Server**: Chosen over nginx/Apache for simplicity in Replit environment
- **Asset Routing Logic**: Automatically handles WordPress path structure without URL rewriting
- **Static Export Approach**: Maintains original design while eliminating PHP/database dependencies
- **Port 5000**: Required by Replit for frontend preview functionality