import time, json, urllib.request
import luma.core.error
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT
from luma.core.render import canvas

# create matrix device
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=32, height=8, block_orientation=-90, rotate=2)


def demo():
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="white")

if __name__ == "__main__":
    try:
        while(True):
            demo()
    except KeyboardInterrupt:
        pass