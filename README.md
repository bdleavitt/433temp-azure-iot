# 433temp-azure-iot
f6cd6a7effe8556d14efdddc3264c64817a4b7fc
433mhz temperature sensors, Raspberry Pi, Azure IoT Hub... what's not to love? 

This is a simple temperature/humidity monitoring use case leveraging 433mhz wireless temp/humidty sensors, Raspberry Pi equipped with a USB antennae, and using python to push values to Azure IoT hub. From there, the possiblities are endless, but I show how to stream data directly into Power BI. 

## Set up and Bill of Materials: 
* Raspberry Pi 3B+ 

## Capturing wireless 433mhz signals:
### 1. Install "rtl-sdr" on raspberry pi following instructions here: https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr 

`git clone git://git.osmocom.org/rtl-sdr.git`

Install dev packages for libusb1.0
`sudo apt-get install libusb-1.0-0-dev`

Note: I had to install cmake first on my RBPi. 
`sudo apt-get install cmake`

```
cd rtl-sdr/
mkdir build
cd build
cmake ../ -DINSTALL_UDEV_RULES=ON
make
sudo make install
sudo ldconfig
```
### 2. Install "rtl_433 on raspberry pi https://github.com/merbanan/rtl_433
Install dependencies: 
`sudo apt-get install libtool libusb-1.0.0-dev librtlsdr-dev rtl-sdr build-essential autoconf cmake pkg-config`

from project root
`git clone https://github.com/merbanan/rtl_433`

```
cd rtl_433/
mkdir build
cd build
cmake ../
make
sudo make install
```
Now, let's test it out. Make sure the USB antennae is plugged in, then From the command line, run the following command: 
`rtl_433 -R 20 -F json -d 0`

The rtl_433 program should initialize, find the 

### 3. 
