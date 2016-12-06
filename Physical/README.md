# Physical Details of the Brain

This folder holds things relating to the physical instantiation of the Brain (rather than the software installed on it).

That includes things like the design files for laser-cut enclosures, and design files for [any custom PCB](BootProgressBoard/).

## Wiring

These wiring details use [this Raspberry Pi GPIO connector diagram](http://elinux.org/RPi_Low-level_peripherals#Model_A.2B.2C_B.2B_and_B2) for labels.

### RFID Reader

|Connector P1 (l-r)|Raspberry Pi|
|------------------|------------|
|VCC|+3V3|
|IN|Not connected|
|SDA|GPIO2/SDA1|
|SCL|GPIO3/SCL1|
|OUT|GPIO4|
|GND|GND|

### BootProgressBoard

|Connector P1 (l-r)|Raspberry Pi|
|------------------|------------|
|1|GPIO24|
|2|GPIO18|
|3|GPIO17|
|4|GPIO27|
|5|GPIO22|
|6|GPIO23|
|7|GPIO10|
|8|+3V3|
|9|GND|

### Raspberry Pi 2/3

Audio is provided by an amplifier board connected to the 3.5mm jack on the Pi.

See [here for a diagram showing the 3.5mm connections](http://www.raspberrypi-spy.co.uk/2014/07/raspberry-pi-model-b-3-5mm-audiovideo-jack/)

|Amp|3.5mm jack on the Pi|
|---|--------------------|
|Left|Tip|
|Right|Ring 1|
|Ground|Ring 2|
|Not connected|Sleeve|

