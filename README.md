# LoRa/LoRaWAN step by step

This projects allow you to test LoRa/LoRaWAN networks from scratch, starting with a point to point LoRa communication, then a little LoRaWAN network using two [ESP32 Oled LoRa](http://www.lilygo.cn/prod_view.aspx?TypeId=50003&Id=1137&FId=t3:50003:3) and an [arduino-uno](https://store.arduino.cc/usa/arduino-uno-rev3)

Microcontrollers code in this repository is formed by forked projects made by this awesome people:

* Aaron.Lee from HelTec AutoMation, ChengDu, China
  成都惠利特自动化科技有限公司
  www.heltec.cn
* Maarten Westenberg (mw12554@hotmail.com),	based on work done by Thomas Telkamp for Raspberry PI 1-ch gateway and many others.
* Thomas Telkamp and Matthijs Kooijman.

## Hardware

* [ESP32 Oled LoRa](http://www.lilygo.cn/prod_view.aspx?TypeId=50003&Id=1137&FId=t3:50003:3)
* [arduino-uno](https://store.arduino.cc/usa/arduino-uno-rev3)

![](img/lorawannetwork.png)

## Development and deploy environment 

[![](https://raw.githubusercontent.com/iiroj/public/master/Visual%20Studio%20Code%20icon/Visual%20Studio%20Code.iconset/icon_128x128%402x.png)](https://go.microsoft.com/fwlink/?LinkID=760868)  
[VS Code](https://go.microsoft.com/fwlink/?LinkID=760868)

[![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.freebiesupply.com%2Flogos%2Fthumbs%2F1x%2Fplatformio-logo.png&f=1&nofb=1)](https://platformio.org/install/ide?install=vscode)  
[PlatformIO IDE](https://platformio.org/install/ide?install=vscode)

[![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.RVsBFjD5vtT-nsOmiL9gAAAAAA%26pid%3DApi&f=1)](https://jupyterlab.readthedocs.io/en/stable/)  
[Jupyterlab](https://jupyterlab.readthedocs.io/en/stable/)


## Instructions

* **[Download and install VSCode](https://code.visualstudio.com/Download)**
* **[Download and install Platformio](https://docs.platformio.org/en/latest/ide/vscode.html)**
* **[Download and install Python3](https://www.python.org/downloads/)**

To **get started** with LoRa, go to `0.oled_lora_sender` and `1.oled_lora_reciever` that code allows you test point to point LoRa connection with two [ESP32 Oled LoRa](http://www.lilygo.cn/prod_view.aspx?TypeId=50003&Id=1137&FId=t3:50003:3).

Then, you can build a one gateway and two nodes LoRaWAN network using  `2.esp32_single_channel_lora_gateway`, `3.esp32_single_channel_lora_node` and `4.arduino_uno_lora_node`.

For each project, from VSCode and `PIO Home`, click in `Open project` option, open the `.ino` file for each project, press `Ctrl + Alt + B`, with ESP32/Arduino connected, press `Ctrl + Alt + u`.

## Documentation

