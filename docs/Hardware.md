# Hardware Targets

The Knob Runtime is hardware agnostic. The following devices are being
used during development and serve as reference implementations.

## Waveshare ESP32-S3 Knob Touch LCD 1.8"

https://www.waveshare.com/esp32-s3-knob-touch-lcd-1.8.htm

Features:
- ESP32-S3
- 360x360 circular LCD
- Capacitive touch
- Rotary encoder
- Wi-Fi / Bluetooth

Status:
- Planned support

---

## ESP32-S3 2.1" Rotary Knob Display

https://www.esp32s.com/product/esp32-s3-development-board-2-1-inch-round-rotary-knob-lcd-smart-screen-2-1inch-display-480x480-lvgl-for-arduino/

Features:
- ESP32-S3
- 480x480 circular LCD
- Capacitive touch
- Rotary encoder with push button
- Wi-Fi / Bluetooth

Status:
- Future support

---

## Hardware Requirements

The runtime does not require a specific device.

A supported device should expose one or more of the following capabilities:

- Display
- Touch
- Rotary Encoder
- Rotary Push Button (optional)
- Haptics (optional)
- Audio (optional)
- USB
- Bluetooth
- Wi-Fi