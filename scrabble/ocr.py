#!/usr/bin/python3

from PIL import Image
from PIL import ImageFilter
import cv2
import pytesseract
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1920, 600)
camera.iso = 600
camera.start_preview()
sleep(1)
camera.capture('/home/pi/scrabble/1.jpg')
camera.stop_preview()

img = Image.open ('1.jpg').convert('L')

blackwhite = img.point(lambda x: 0 if x < 66 else 255, '1')
blackwhite.save("1bw.jpg")

im = Image.open("1bw.jpg")
smooth_im = im.filter(ImageFilter.SMOOTH_MORE)

text = pytesseract.image_to_string(smooth_im, config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ -psm 7')

print(text)
exit