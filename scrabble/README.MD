# Scrabble Word Finder

The scrabble word finder is a project that allows the raspberry pi to look at a set of scrabble tiles and output to a connected screen, the top most highest scoring words that can be used from those letters

Note that you would still have to find a place to be able to play one of those words on the scrabble board

## Important Notes

This library is not what I would call 'plug and play'. Installation was complex, and the image parsing library took a lot of fiddling to get a readable picture. Slight changes in lighting made the letters unreadable. 

**You will have to fiddle with the code.**

## Installation

This assumes you have Python 3 installed.

Installation was complicated, because the default way of installing should be

`sudo apt-get install tesseract-ocr`

however, that installs (at time of writing) version 4 of tesseract, which does not work with a whitelist. 

Many atempts were made to use `--oem 0` with tesseract 4 to enable whitelisting, but then more errors sprang up about needing dictionaries.

Therefore the solution was to compile the library locally from the source using these commands:

* git clone --depth 1  https://github.com/tesseract-ocr/tesseract.git 
* cd tesseract-ocr/
* ./autogen.sh
* ./configure
* make
* sudo make install
* sudo ldconfig
* tesseract -v

Then you must download the english trained data from: [https://github.com/tesseract-ocr/tessdata/blob/master/eng.traineddata](https://github.com/tesseract-ocr/tessdata/blob/master/eng.traineddata)

Then you need to set an environment variable to the location of that english trained data.

You can use `export TESSDATA_PREFIX=/home/pi/tesseract/tessdata` (replacing the location with the location of the folder you downloaded the traineddata into) in your CLI or add this to your `~/.bashrc` to ensure it is set on startup 

You may or may not need to install the following dependencies, which allow Optical Character Recognition:

`sudo apt install libsm6 libxrender1 libfontconfig1 libatlas3-base libqtgui4 libqt4-test libwebp6 libtiff5 libjasper1 libilmbase12 libopenexr22 libilmbase12 libgstreamer1.0-0 libavcodec57 libavformat57 libavutil55 libswscale4 libqtgui4 libqt4-test libqtcore4`

You may also need to run a `sudo apt update`

You also need to use pip3 to install
```
pip3 install opencv-python==3.4.6.27
pip3 install pytesseract
pip3 install time
pip3 install PySimpleGUI
pip3 install Image
```

Source: https://raspberrypi.stackexchange.com/questions/89231/tesseract-ocr-4-x-beta-for-raspberry-pi

## Running The Libarary
Simply run `python3 scrabbleWordFinder.py`