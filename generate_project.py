#!/usr/bin/env python3
import os
import shutil

def create_dirs():
    """إنشاء المجلدات الضرورية فقط"""
    dirs = [
        "android-project/app/src/main/java/com/mediaserver/pro",
        "android-project/app/src/main/res/layout",
        "android-project/app/src/main/res/values", 
        "android-project/app/src/main/assets",
        "templates"
    ]
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"✅ Created: {dir_path}")

def copy_files():
    """نسخ الملفات الأساسية فقط"""
    templates = {
        "AndroidManifest.xml": "android-project/app/src/main/AndroidManifest.xml",
        "MainActivity.java": "android-project/app/src/main/java/com/mediaserver/pro/MainActivity.java",
        "activity_main.xml": "android-project/app/src/main/res/layout/activity_main.xml",
        "strings.xml": "android-project/app/src/main/res/values/strings.xml",
        "build.gradle": "android-project/app/build.gradle"
    }
    
    for src, dst in templates.items():
        if os.path.exists(f"templates/{src}"):
            shutil.copy(f"templates/{src}", dst)
            print(f"✅ Copied: {src}")

def create_gradle_files():
    """إنشاء ملفات Gradle الأساسية"""
    # ملف gradle wrapper بسيط
    gradlew_content = '''#!/bin/sh
echo "Gradle wrapper placeholder"
exit 0
'''
    with open("android-project/gradlew", "w") as f:
        f.write(gradlew_content)
    os.chmod("android-project/gradlew", 0o755)
    
    # ملف build.gradle للمشروع الرئيسي
    build_gradle = '''plugins {
    id 'com.android.application'
}

android {
    compileSdk 34
    defaultConfig {
        applicationId "com.mediaserver.pro"
        minSdk 21
        targetSdk 34
        versionCode 1
        versionName "1.0.0"
    }
    buildTypes {
        release {
            minifyEnabled false
        }
    }
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.10.0'
}
'''
    with open("android-project/build.gradle", "w") as f:
        f.write(build_gradle)

def main():
    print("🚀 Starting project generation...")
    
    # تنظيف إن وجد
    if os.path.exists("android-project"):
        shutil.rmtree("android-project")
    
    create_dirs()
    copy_files()
    create_gradle_files()
    
    print("✅ Project generated successfully!")
    print("📱 APK will be built by GitHub Actions")

if __name__ == "__main__":
    main()