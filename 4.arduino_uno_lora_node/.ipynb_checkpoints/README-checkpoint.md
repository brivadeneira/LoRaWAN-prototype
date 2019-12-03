# Arduino UNO node

This code allows you to set up a LoRaWAN node using **[arduino uno](https://store.arduino.cc/usa/arduino-uno-rev3)** and [Shield eMGing LoRa](http://emging.com.ar/producto/shield-emging-lora-v1-1-915mhz-rfm95w/).

![](https://cdn-tienda.bricogeek.com/1157-thickbox_default/arduino-uno.jpg)
![](https://emging.com.ar/wp-content/uploads/2019/09/IMG_2600.jpg)

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
* Click in `Open project` option, open the `arduino-uno-lora-shield.ino` file
* Change `NwkSKey`, `APPSKEY` and `DEVADDR` according to `overview` information of the dev in ttn:

```shell=ino
// LoRaWAN NwkSKey, network session key
// This is the default Semtech key, which is used by the prototype TTN
// network initially.
static const PROGMEM u1_t NWKSKEY[16] = { 0xC3, 0x88, 0xDB, 0x4C, 0x99, 0x7B, 0x0A, 0x3D, 0xD5, 0x6E, 0x8B, 0xF3, 0xFD, 0x8F, 0x3B, 0x86 };

// LoRaWAN AppSKey, application session key
// This is the default Semtech key, which is used by the prototype TTN
// network initially.
static const u1_t PROGMEM APPSKEY[16] = { 0x9B, 0xC7, 0x36, 0x6F, 0xCF, 0x05, 0x7F, 0x9C, 0x30, 0xB6, 0xBD, 0xAC, 0x92, 0x2E, 0x82, 0xFD };

// LoRaWAN end-device address (DevAddr)
// See http://thethingsnetwork.org/wiki/AddressSpace
static const u4_t DEVADDR = 0x2601105B ; // <-- Change this address for every node!
```

> from line 32 to 44.

* Press `Ctrl + Alt + B` to build.
* with ESP32 connected, press `Ctrl + Alt + u` to upload the code.