#!/usr/bin/env python3
"""
build_deploy.py
Builds the Vite project inside _source/ and deploys compiled assets directly to the repository root.
"""
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ROOT, "_source")
SOURCE_DIST = os.path.join(SOURCE, "dist")

def run_cmd(cmd, cwd):
    print(f"Running command: {' '.join(cmd)} in {cwd}")
    result = subprocess.run(cmd, cwd=cwd, shell=False)
    if result.returncode != 0:
        print(f"Error executing command: {' '.join(cmd)}")
        sys.exit(result.returncode)

def main():
    print("==========================================")
    print("Building Vite frontend inside _source/...")
    
    # Run npm install if node_modules doesn't exist inside _source/
    node_modules_dir = os.path.join(SOURCE, "node_modules")
    if not os.path.exists(node_modules_dir):
        print("node_modules/ not found inside _source/, running npm install...")
        run_cmd(["npm", "install"], cwd=SOURCE)

    run_cmd(["npx", "vite", "build", "--base", "./"], cwd=SOURCE)
    
    if not os.path.exists(SOURCE_DIST):
        print("Error: dist/ directory was not created inside _source/.")
        sys.exit(1)
        
    # Remove old compiled assets in the root
    root_index = os.path.join(ROOT, "index.html")
    root_assets = os.path.join(ROOT, "assets")
    
    if os.path.exists(root_index):
        print("Removing old root index.html...")
        os.remove(root_index)
        
    if os.path.exists(root_assets):
        print("Removing old root assets/ directory...")
        shutil.rmtree(root_assets)
        
    # Copy new compiled assets to the root
    print("Copying new compiled index.html to root...")
    shutil.copy2(os.path.join(SOURCE_DIST, "index.html"), root_index)
    
    print("Copying new compiled assets/ to root...")
    os.makedirs(root_assets, exist_ok=True)
    for item in os.listdir(os.path.join(SOURCE_DIST, "assets")):
        src = os.path.join(SOURCE_DIST, "assets", item)
        dest = os.path.join(root_assets, item)
        shutil.copy2(src, dest)
        
    # Clean up dist folder inside _source/
    print("Cleaning up _source/dist/...")
    shutil.rmtree(SOURCE_DIST)
    
    print("==========================================")
    print("Build and Deployment Packaging to Root Complete!")
    print("==========================================")

if __name__ == "__main__":
    main()
