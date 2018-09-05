# 433temp-azure-iot

433mhz temperature sensors, Raspberry Pi, Azure IoT Hub... what's not to love? 

This is a simple temperature/humidity monitoring use case leveraging 433mhz wireless temp/humidty sensors, Raspberry Pi equipped with a USB antennae, and using python to push values to Azure IoT hub. From there, the possiblities are endless, but I show how to stream data directly into Power BI. 

## Set up and Bill of Materials: 
* Raspberry Pi 3B+ 

## Capturing wireless 433mhz signals:
1. Install "rtl-sdr" on raspberry pi following instructions here: https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr 

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


2. Install "rtl_433 on raspberry pi https://github.com/merbanan/rtl_433
