# Devscover Tutorials

This repository contains the various tutorials written for either [Devscover.com](www.devscover.com) or the [Devscover YouTube channel](https://youtube.com/c/devscover?sub_confirmation=1).

## Reccomendations For Raspberry Pi
1) Install support for ExFat USB devices
    - ```sudo apt-get install exfat-fuse```
    - ```sudo apt-get install exfat-utils```
    
2) Increase your screen resolution
    - For HDMI:
        ```sudo raspi-config > advanced > resolution```
    - For Official Touchscreen
        ```
        cd /boot
        sudo nano config.txt
          
        framebuffer_width=1024
        framebuffer_height=614
      ```

## Tutorials
### https://youtube.com/c/devscover