# LoRa/LoRaWAN step by step

This group of projects allows you to test LoRa/LoRaWAN networks from scratch.

## Hardware

* ESP32 + OLED + RFM95 + antenna (x2)
* Arduino UNO + Shield
* Raspberry Pi 3 + Shield

## Requirements

[VS Code](https://go.microsoft.com/fwlink/?LinkID=760868) + [PlatformIO IDE](https://platformio.org/install/ide?install=vscode) are used in this project on Debian 10.

## Instructions

From VSCode and `PIO Home`, click in `Open project` option, open the `.ino` file for each project, press `Ctrl + Alt + B`, with ESP32/Arduino/Raspi connected, click in `->` (upload)

## Projects

*Each project has its own README file with the instructions*

* **OLED_LoRa_Sender**
* **OLED_LoRa_Reciever**

both of them to test point to point LoRa network using ESP32 hardware.

* **ESP32SingleChannelGateway**