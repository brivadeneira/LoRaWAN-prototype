# ESP32 node

This code allows you to set up a LoRaWAN node using **[ESP32 Oled LoRa](http://www.lilygo.cn/prod_view.aspx?TypeId=50003&Id=1137&FId=t3:50003:3)**.

* Register an account in [thethingsnetwork](https://www.thethingsnetwork.org/)
* Go to `console` clicking in your avatar.
* Go to `application`

![](https://i.imgur.com/ptdWS4E.png)

* Click in `add aplication`:

![](https://i.imgur.com/ZiiYfbV.png)

* Go to `devices` and click in `register device`.

![](https://i.imgur.com/XR09sao.png)

* Choose a dev ID, then click in `generate` for `Device EUI` field:

![](https://i.imgur.com/YJI3zuN.png)

* Go to `settings`, change OTAA activation for ABP.
* Go to `overview`, look hexa keys *(press `<>`)*.

![](https://i.imgur.com/aTrRETH.png)

* Go to VSCode and `PIO Home`
* Click in `Open project` option, open the `esp32-node.ino` file
* Change `NwkSKey`, `APPSKEY` and `DEVADDR` according to `overview` information of the dev in ttn:

```
// LoRaWAN NwkSKey, network session key
static const PROGMEM u1_t NWKSKEY[16] = { 0xCC, 0x5B, 0xBB, 0x45, 0x3B, 0x8B, 0xD9, 0x51, 0x57, 0x72, 0x22, 0x41, 0x7C, 0x95, 0x34, 0xD1 };
// LoRaWAN AppSKey, application session key
static const u1_t PROGMEM APPSKEY[16] = { 0xDE, 0xD0, 0xDD, 0xE8, 0x2C, 0xFC, 0x28, 0x7F, 0x66, 0x90, 0x82, 0x74, 0x9B, 0x87, 0xA0, 0x35 };
// LoRaWAN end-device address (DevAddr)
static const u4_t DEVADDR = { 0x26011FEE };
```

> from line 13 to 18.

* Press `Ctrl + Alt + B` to build.
* with ESP32 connected, press `Ctrl + Alt + u` to upload the code.