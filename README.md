# 🍕 Pizza Empire – Merge & Cook (Flutter app)

The full game runs inside the app and works **offline**. It includes:
- 100 stages and 10 outlets
- the 3D restaurant
- upgrades, staff, daily rewards and achievements
- auto-save on the phone

## 1. Requirements
- Flutter 3.24 or newer: https://docs.flutter.dev/get-started/install
- Android Studio with an Android SDK, or Xcode for iPhone

## 2. Set up (one time)
Open a terminal in this folder and run:
```
flutter create --org com.yourname --project-name pizza_empire --platforms android,ios .
flutter pub get
dart run flutter_launcher_icons
```
`flutter create` adds the android/ and ios/ folders. It keeps your existing lib/, assets/ and pubspec.yaml.

Then change the app name shown on the phone:
- **Android:** in `android/app/src/main/AndroidManifest.xml`, set `android:label="Pizza Empire"`
- **iOS:** in `ios/Runner/Info.plist`, set `CFBundleDisplayName` to `Pizza Empire`

Optional, for vibration on Android: add this line above `<application` in AndroidManifest.xml:
```
<uses-permission android:name="android.permission.VIBRATE"/>
```

## 3. Run on your phone
Connect the phone with USB debugging on, then run:
```
flutter run
```

## 4. Build an installable APK
```
flutter build apk --release
```
The APK is at `build/app/outputs/flutter-apk/app-release.apk`. Copy it to your phone and install it.

For the Play Store, build an app bundle instead:
```
flutter build appbundle --release
```
You'll need to set up a signing key first: https://docs.flutter.dev/deployment/android

## Project layout
```
lib/main.dart            Full-screen WebView, back button, portrait lock, splash
assets/game/index.html   The complete game (gameplay, 3D, saves)
assets/game/three.min.js 3D engine, bundled so the game works offline
assets/icon/icon.png     App icon
```

## Updating the game
Replace `assets/game/index.html` with a newer version and rebuild.
All game rules, recipes and stage settings are in the CONFIG section near the top of that file.

## Android back button
- Closes an open dialog
- Pauses during a stage
- Goes back from the stage list to the outlets
- Exits the app from the outlet screen

## Credits
Character skeleton, mannequin body and animations: KayKit Character Animations by Kay Lousberg (kaylousberg.com), CC0.
