# Ferozo Hosting Deployment Workflow

This repository has been structured specifically for seamless deployment onto Ferozo (or any Apache/PHP hosting environment). The root of the repository directly represents the production environment, while development files are isolated.

## Project Structure

```
prepsecplus/ (Repository Root / Production Deployment Folder)
├── _source/                  # Development source files (isolated)
│   ├── package.json          # Node dependencies and scripts
│   ├── app.js                # Core JS logic
│   ├── style.css             # Vanilla styling
│   ├── index.html            # Dev entrypoint
│   └── node_modules/         # Local dev packages (ignored by Git)
├── assets/                   # Compiled Vite JS/CSS chunks (tracked by Git)
├── index.html                # Compiled entrypoint (tracked by Git)
├── contact.php               # PHP backend for email forms
├── .htaccess                 # Apache SPA routing rules
├── robots.txt                # SEO search robot controls
├── sitemap.xml               # SEO website index
├── favicon.ico               # Website favicon
├── *.json                    # Study database payload files (study_days.json, questions.json, etc.)
├── *.md                      # Narrative reading modules
├── audio/                    # Directory for .mp3 files (ignored by Git)
├── video/                    # Directory for .mp4 files (ignored by Git)
├── *.zip                     # Heavy zip archives (ignored by Git)
└── build_deploy.py           # Local build automation script
```

## How to Build Locally

To compile changes made to development files (inside `_source/`):

1. Make sure Python 3 is installed.
2. Run the automation script in the repository root:
   ```bash
   python3 build_deploy.py
   ```
3. This script will:
   - Run Vite compilation inside `_source/`.
   - Remove the old compiled `index.html` and `assets/` folder in the root.
   - Copy the newly compiled `index.html` and `assets/` from `_source/dist/` directly into the repository root.
   - Clean up temporary build artifacts in `_source/dist/`.

## Deploying to Ferozo

### Method A: Automated Deployment via Git (Recommended)

1. Connect your Ferozo hosting to pull directly from your private GitHub repository `master` branch.
2. Build files locally and commit the compiled changes:
   ```bash
   python3 build_deploy.py
   git add .
   git commit -m "Build and update compiled production assets"
   git push origin master
   ```
3. Since the repository root is exactly the compiled website layout, pushing to GitHub will deploy it instantly to your Ferozo web directory (under `/public_html/splus/`).

### Method B: Manual Deployment via FTP/File Manager

If you are not using Git integration on the Ferozo server:
1. Run the local build script:
   ```bash
   python3 build_deploy.py
   ```
2. Using an FTP client (e.g. FileZilla) or the Ferozo Control Panel File Manager, upload all files and directories in the repository root **except the `_source/` folder** directly to `/public_html/splus/` on your server.
3. Upload the `audio/` and `video/` folders containing `.mp3` and `.mp4` files (and any `.zip` files) directly to `/public_html/splus/` on your server.
