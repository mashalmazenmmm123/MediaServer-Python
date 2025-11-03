#!/usr/bin/env python3
import os
import shutil

def create_project_structure():
    """إنشاء هيكل المشروع الكامل"""
    # تنظيف أولاً
    if os.path.exists("android-project"):
        shutil.rmtree("android-project")
    
    # إنشاء المجلدات الأساسية
    base_dirs = [
        "android-project/app/src/main/java/com/mediaserver/pro",
        "android-project/app/src/main/res/layout",
        "android-project/app/src/main/res/values",
        "android-project/app/src/main/res/drawable",
        "android-project/app/src/main/assets",
        "android-project/gradle/wrapper",
        "templates"
    ]
    
    for dir_path in base_dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"✅ Created: {dir_path}")

def create_gradle_files():
    """إنشاء ملفات Gradle الأساسية"""
    
    # ملف gradle/wrapper/gradle-wrapper.properties
    wrapper_properties = """distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\\://services.gradle.org/distributions/gradle-8.4-bin.zip
networkTimeout=10000
validateDistributionUrl=true
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
"""
    os.makedirs("android-project/gradle/wrapper", exist_ok=True)
    with open("android-project/gradle/wrapper/gradle-wrapper.properties", "w") as f:
        f.write(wrapper_properties)
    
    # ملف gradlew (Gradle wrapper)
    gradlew_content = """#!/usr/bin/env sh

# Gradle wrapper script
echo "Gradle Wrapper - Placeholder"
echo "This will be replaced by actual gradlew during build"
"""
    with open("android-project/gradlew", "w") as f:
        f.write(gradlew_content)
    os.chmod("android-project/gradlew", 0o755)
    
    # ملف build.gradle للمشروع الرئيسي
    root_build_gradle = """plugins {
    id 'com.android.application' version '8.1.0' apply false
}

task clean(type: Delete) {
    delete rootProject.buildDir
}
"""
    with open("android-project/build.gradle", "w") as f:
        f.write(root_build_gradle)
    
    # ملف build.gradle للتطبيق
    app_build_gradle = """plugins {
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
        
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
        debug {
            debuggable true
        }
    }
    
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
    
    buildFeatures {
        viewBinding true
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.10.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
    
    testImplementation 'junit:junit:4.13.2'
    androidTestImplementation 'androidx.test.ext:junit:1.1.5'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.5.1'
}
"""
    with open("android-project/app/build.gradle", "w") as f:
        f.write(app_build_gradle)
    
    # ملف settings.gradle
    settings_gradle = """pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "MediaServerPro"
include ':app'
"""
    with open("android-project/settings.gradle", "w") as f:
        f.write(settings_gradle)

def copy_template_files():
    """نسخ ملفات القوالب"""
    templates = {
        "AndroidManifest.xml": "android-project/app/src/main/AndroidManifest.xml",
        "MainActivity.java": "android-project/app/src/main/java/com/mediaserver/pro/MainActivity.java",
        "activity_main.xml": "android-project/app/src/main/res/layout/activity_main.xml",
        "strings.xml": "android-project/app/src/main/res/values/strings.xml",
    }
    
    for template_file, destination in templates.items():
        if os.path.exists(f"templates/{template_file}"):
            shutil.copy(f"templates/{template_file}", destination)
            print(f"✅ Copied: {template_file}")

def main():
    print("🚀 Starting Android project generation...")
    
    create_project_structure()
    create_gradle_files()
    copy_template_files()
    
    print("✅ Android project generated successfully!")
    print("📁 Project structure created")
    print("🔧 Gradle files configured")
    print("📋 Template files copied")

if __name__ == "__main__":
    main()