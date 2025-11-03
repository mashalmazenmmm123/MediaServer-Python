#!/usr/bin/env python3
from generate_project import main as generate_project

def build_apk():
    print("🚀 Building APK...")
    generate_project()
    print("✅ Build completed!")

if __name__ == "__main__":
    build_apk()
