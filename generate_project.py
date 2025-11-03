#!/usr/bin/env python3
import os
import shutil

def create_simple_project():
    """إنشاء مشروع بسيط"""
    if os.path.exists("android-project"):
        shutil.rmtree("android-project")
    
    # إنشاء المجلدات الأساسية فقط
    dirs = [
        "android-project/app/src/main/java/com/mediaserver/pro",
        "android-project/app/src/main/res/layout",
        "android-project/app/src/main/res/values",
    ]
    
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    
    # إنشاء ملفات Gradle الأساسية
    create_gradle_files()
    
    # نسخ ملفات التطبيق
    copy_app_files()

def create_gradle_files():
    """إنشاء ملفات Gradle الأساسية"""
    
    # ملف settings.gradle
    with open("android-project/settings.gradle", "w") as f:
        f.write("include ':app'\n")
    
    # ملف build.gradle الرئيسي
    with open("android-project/build.gradle", "w") as f:
        f.write("""
plugins {
    id 'com.android.application' version '8.1.0' apply false
}
""")
    
    # ملف build.gradle للتطبيق
    with open("android-project/app/build.gradle", "w") as f:
        f.write("""
plugins {
    id 'com.android.application'
}

android {
    namespace 'com.mediaserver.pro'
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
        debug {
            debuggable true
        }
    }
    
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
}
""")

def copy_app_files():
    """نسخ ملفات التطبيق الأساسية"""
    
    # AndroidManifest.xml
    with open("android-project/app/src/main/AndroidManifest.xml", "w") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.mediaserver.pro">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="Media Server"
        android:theme="@style/Theme.AppCompat.Light.DarkActionBar">
        
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
""")
    
    # MainActivity.java
    with open("android-project/app/src/main/java/com/mediaserver/pro/MainActivity.java", "w") as f:
        f.write("""package com.mediaserver.pro;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        TextView textView = new TextView(this);
        textView.setText("Media Server Pro - Hello World!");
        textView.setTextSize(20);
        setContentView(textView);
    }
}
""")
    
    # activity_main.xml
    with open("android-project/app/src/main/res/layout/activity_main.xml", "w") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="20dp">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Media Server Pro"
        android:textSize="24sp"
        android:textStyle="bold" />
        
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Built with GitHub Actions"
        android:textSize="16sp"
        android:layout_marginTop="10dp" />

</LinearLayout>
""")
    
    # strings.xml
    with open("android-project/app/src/main/res/values/strings.xml", "w") as f:
        f.write("""<resources>
    <string name="app_name">Media Server Pro</string>
</resources>
""")

def main():
    print("🚀 Creating simple Android project...")
    create_simple_project()
    print("✅ Project created successfully!")
    print("📱 Ready to build APK")

if __name__ == "__main__":
    main()