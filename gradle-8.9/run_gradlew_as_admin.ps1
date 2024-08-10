Start-Process powershell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command ".\gradlew.bat clean build --debug"' -Verb RunAs
