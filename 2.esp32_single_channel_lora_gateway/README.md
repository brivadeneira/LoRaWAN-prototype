# ESP32 Gateway

This code allows you to get a LoRaWAN gateway in one **[ESP32 Oled LoRa](http://www.lilygo.cn/prod_view.aspx?TypeId=50003&Id=1137&FId=t3:50003:3)**.

![](https://i.imgur.com/tXObZ6c.jpg)

* Go to VSCode and `PIO Home`
* Click in `Open project` option, open the `esp32-gateway.ino` file
* Press `Ctrl + Alt + B` to build.
* with ESP32 connected, press `Ctrl + Alt + u` to upload the code.

Go to [thethingsnetwork](), register an account, go to `console` and click in `gateways`:

![](https://i.imgur.com/Z3LTCU9.png)

**Register a new gateway**:

* `Gateway ID`: *Go to serial monitor in PlatformIO and look the number, for example: 240AC4FFFF309B28.
* `Frequency plan`: United States 915 MHz.
* `Location`: Get latitude and longitude, for example: -33.113412332923005, -64.3284786120057.
* `Antenna Placement`: Indoor.

* Go to `3.esp32_single_channel_lora_node`.

> For more details look [vpcola](https://github.com/vpcola) guide [Vergil Cola](https://www.youtube.com/channel/UCRk1KlFXVkJXH2IKpdQsW0g).

> **ERROR**: `/home/bibiana/usr/arduino-1.8.10/libraries/IBM_LMIC_framework/src/lmic/radio.c:689`
> **SOLUCIÓN**: `nano /home/bibiana/usr/arduino-1.8.10/libraries/IBM_LMIC_framework/src/hal/hal.cpp`
> Cambiar `SPI.begin().` por `SPI.begin(5,19,27,18);`
> *Fuente: [Foro thethingsnetworks "BIG ESP32 / SX127x topic part 1](https://www.thethingsnetwork.org/forum/t/big-esp32-sx127x-topic-part-1/10247/130).*
