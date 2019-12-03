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