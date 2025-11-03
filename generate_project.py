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
        "android-project/gradle/wrapper",
    ]
    
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    
    # إنشاء ملفات Gradle الأساسية
    create_gradle_files()
    
    # نسخ ملفات التطبيق
    copy_app_files()
    
    # إنشاء gradlew
    create_gradlew()

def create_gradle_files():
    """إنشاء ملفات Gradle الأساسية"""
    
    # ملف settings.gradle
    with open("android-project/settings.gradle", "w") as f:
        f.write("""
pluginManagement {
    repositories {
        gradlePluginPortal()
        google()
        mavenCentral()
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
""")
    
    # ملف build.gradle الرئيسي
    with open("android-project/build.gradle", "w") as f:
        f.write("""
// Top-level build file where you can add configuration options common to all sub-projects/modules.
plugins {
    id 'com.android.application' version '8.1.0' apply false
}

task clean(type: Delete) {
    delete rootProject.buildDir
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
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
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
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
}
""")
    
    # ملف gradle/wrapper/gradle-wrapper.properties
    with open("android-project/gradle/wrapper/gradle-wrapper.properties", "w") as f:
        f.write("""#Mon Sep 02 22:20:17 CEST 2024
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\\://services.gradle.org/distributions/gradle-8.4-all.zip
networkTimeout=10000
validateDistributionUrl=true
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
""")

def create_gradlew():
    """إنشاء ملف gradlew"""
    gradlew_content = """#!/usr/bin/env sh

#
# Copyright 2015 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

##############################################################################
##
##  Gradle start up script for UN*X
##
##############################################################################

# Attempt to set APP_HOME
# Resolve links: $0 may be a link
PRG="$0"
# Need this for relative symlinks.
while [ -h "$PRG" ] ; do
    ls=$(ls -ld "$PRG")
    link=$(expr "$ls" : '.*-> \\(.*\\)$')
    if expr "$link" : '/.*' > /dev/null; then
        PRG="$link"
    else
        PRG=$(dirname "$PRG")"/$link"
    fi
done
SAVED="`pwd`"
cd "`dirname \"$PRG\"`/" >/dev/null
APP_HOME="`pwd -P`"
cd "$SAVED" >/dev/null

APP_NAME="Gradle"
APP_BASE_NAME=$(basename "$0")

# Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
DEFAULT_JVM_OPTS='"-Xmx64m" "-Xms64m"'

# Use the maximum available, or set MAX_FD != -1 to use that value.
MAX_FD="maximum"

warn () {
    echo "$*"
}

die () {
    echo
    echo "$*"
    echo
    exit 1
}

# OS specific support (must be 'true' or 'false').
cygwin=false
msys=false
darwin=false
nonstop=false
case "`uname`" in
  CYGWIN* )
    cygwin=true
    ;;
  Darwin* )
    darwin=true
    ;;
  MINGW* )
    msys=true
    ;;
  NONSTOP* )
    nonstop=true
    ;;
esac

CLASSPATH=$APP_HOME/gradle/wrapper/gradle-wrapper.jar

# Determine the Java command to use to start the JVM.
if [ -n "$JAVA_HOME" ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
        # IBM's JDK on AIX uses strange locations for the executables
        JAVACMD="$JAVA_HOME/jre/sh/java"
    else
        JAVACMD="$JAVA_HOME/bin/java"
    fi
    if [ ! -x "$JAVACMD" ] ; then
        die "ERROR: JAVA_HOME is set to an invalid directory: $JAVA_HOME

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
    fi
else
    JAVACMD="java"
    which java >/dev/null 2>&1 || die "ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
fi

# Increase the maximum file descriptors if we can.
if [ "$cygwin" = "false" -a "$darwin" = "false" -a "$nonstop" = "false" ] ; then
    MAX_FD_LIMIT=$(ulimit -H -n)
    if [ $? -eq 0 ] ; then
        if [ "$MAX_FD" = "maximum" -o "$MAX_FD" = "max" ] ; then
            MAX_FD="$MAX_FD_LIMIT"
        fi
        ulimit -n $MAX_FD
        if [ $? -ne 0 ] ; then
            warn "Could not set maximum file descriptor limit: $MAX_FD"
        fi
    else
        warn "Could not query maximum file descriptor limit: $MAX_FD_LIMIT"
    fi
fi

# For Darwin, add options to specify how the application appears in the dock
if $darwin; then
    GRADLE_OPTS="$GRADLE_OPTS \"-Xdock:name=$APP_NAME\" \"-Xdock:icon=$APP_HOME/media/gradle.icns\""
fi

# For Cygwin or MSYS, switch paths to Windows format before running java
if [ "$cygwin" = "true" -o "$msys" = "true" ] ; then
    APP_HOME=$(cygpath --path --mixed "$APP_HOME")
    CLASSPATH=$(cygpath --path --mixed "$CLASSPATH")
    JAVACMD=$(cygpath --unix "$JAVACMD")

    # We build the pattern for arguments to be converted via cygpath
    ROOTDIRSRAW=$(find -L / -maxdepth 1 -mindepth 1 -type d 2>/dev/null)
    SEP=""
    for dir in $ROOTDIRSRAW ; do
        ROOTDIRS="$ROOTDIRS$SEP$dir"
        SEP="|"
    done
    OURCYGPATTERN="(^($ROOTDIRS))"
    # Add a user-defined pattern to the cygpath arguments
    if [ "$GRADLE_CYGPATTERN" != "" ] ; then
        OURCYGPATTERN="$OURCYGPATTERN|($GRADLE_CYGPATTERN)"
    fi
    # Now convert the arguments - kludge to limit ourselves to /bin/sh
    i=0
    for arg in "$@" ; do
        CHECK=$(echo "$arg"|egrep -c "$OURCYGPATTERN" -)
        CHECK2=$(echo "$arg"|egrep -c "^-")"                                 ### Determine if an option

        if [ $CHECK -ne 0 ] && [ $CHECK2 -eq 0 ] ; then                      ### Added a condition
            eval $(echo args$i)=$(cygpath --path --ignore --mixed "$arg")
        else
            eval $(echo args$i)=$arg
        fi
        i=$(($i+1))
    done
    case $i in
        0) set -- ;;
        1) set -- "$args0" ;;
        2) set -- "$args0" "$args1" ;;
        3) set -- "$args0" "$args1" "$args2" ;;
        4) set -- "$args0" "$args1" "$args2" "$args3" ;;
        5) set -- "$args0" "$args1" "$args2" "$args3" "$args4" ;;
        6) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" ;;
        7) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" ;;
        8) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" "$args7" ;;
        9) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" "$args7" "$args8" ;;
    esac
fi

# Escape application args
save () {
    for i do printf %s\\\\n "$i" | sed "s/'/'\\\\\\\\''/g;1s/^/'/;\\$s/\\$/' \\\\\\\\/" ; done
    echo " "
}
APP_ARGS=$(save "$@")

# Collect all arguments for the java command, following the shell quoting and substitution rules
eval set -- $DEFAULT_JVM_OPTS $JAVA_OPTS $GRADLE_OPTS "\\\"-Dorg.gradle.appname=$APP_BASE_NAME\\\"" -classpath "\\\"$CLASSPATH\\\"" org.gradle.wrapper.GradleWrapperMain "$APP_ARGS"

exec "$JAVACMD" "$@"
"""
    
    with open("android-project/gradlew", "w") as f:
        f.write(gradlew_content)
    
    # جعل الملف قابل للتنفيذ
    os.chmod("android-project/gradlew", 0o755)

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
        android:label="Media Server Pro"
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
import android.widget.Button;
import android.widget.TextView;
import android.view.View;

public class MainActivity extends Activity {
    
    private TextView statusText;
    private Button startButton;
    private boolean isRunning = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        statusText = findViewById(R.id.statusText);
        startButton = findViewById(R.id.startButton);
        
        startButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!isRunning) {
                    startServer();
                } else {
                    stopServer();
                }
            }
        });
        
        updateUI();
    }
    
    private void startServer() {
        isRunning = true;
        statusText.setText("Server: RUNNING");
        startButton.setText("Stop Server");
        // Here you can add your server logic
    }
    
    private void stopServer() {
        isRunning = false;
        statusText.setText("Server: STOPPED");
        startButton.setText("Start Server");
        // Here you can stop your server
    }
    
    private void updateUI() {
        statusText.setText("Server: STOPPED");
        startButton.setText("Start Server");
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
    android:padding="20dp"
    android:background="#f5f5f5">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Media Server Pro"
        android:textSize="24sp"
        android:textStyle="bold"
        android:textColor="#2196F3"
        android:gravity="center"
        android:layout_marginBottom="30dp" />

    <TextView
        android:id="@+id/statusText"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Server: STOPPED"
        android:textSize="18sp"
        android:textColor="#F44336"
        android:gravity="center"
        android:padding="15dp"
        android:background="#FFFFFF"
        android:layout_marginBottom="20dp" />

    <Button
        android:id="@+id/startButton"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Start Server"
        android:textSize="16sp"
        android:textColor="#FFFFFF"
        android:background="#4CAF50"
        android:padding="15dp" />

</LinearLayout>
""")
    
    # strings.xml
    with open("android-project/app/src/main/res/values/strings.xml", "w") as f:
        f.write("""<resources>
    <string name="app_name">Media Server Pro</string>
</resources>
""")

def main():
    print("🚀 Creating Android project with Gradle wrapper...")
    create_simple_project()
    print("✅ Project created successfully!")
    print("📱 Gradle wrapper included")
    print("🔧 Ready to build APK")

if __name__ == "__main__":
    main()