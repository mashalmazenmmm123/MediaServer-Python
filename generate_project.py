#!/usr/bin/env python3
import os
import shutil

def create_dirs():
    dirs = [
        "android-project/app/src/main/java/com/mediaserver/pro",
        "android-project/app/src/main/res/layout",
        "android-project/app/src/main/res/values", 
        "android-project/app/src/main/assets",
        "templates"
    ]
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)
        print(f"📁 Created: {dir}")

def copy_files():
    templates = {
        "AndroidManifest.xml": "android-project/app/src/main/AndroidManifest.xml",
        "MainActivity.java": "android-project/app/src/main/java/com/mediaserver/pro/MainActivity.java",
        "activity_main.xml": "android-project/app/src/main/res/layout/activity_main.xml",
        "strings.xml": "android-project/app/src/main/res/values/strings.xml",
        "build.gradle": "android-project/app/build.gradle",
        "web_page.html": "android-project/app/src/main/assets/web_page.html"
    }
    for src, dst in templates.items():
        if os.path.exists(f"templates/{src}"):
            shutil.copy(f"templates/{src}", dst)
            print(f"📄 Copied: {src}")

def main():
    print("🚀 Starting project generation...")
    if os.path.exists("android-project"):
        shutil.rmtree("android-project")
    create_dirs()
    copy_files()
    print("✅ Project generated successfully!")

if __name__ == "__main__":
    main()
