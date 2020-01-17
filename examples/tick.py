import time, json, urllib.request
import luma.core.error
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT

def demo():
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=32, height=8, block_orientation=-90, rotate=2)

    # Create The Message
    msg = "Devscover Subscribers: "

    try:
        url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UC7jBsNZf-wRyJkEmDKBrg2A&key=AIzaSyBM34pgtcsM7Mx0DXojsSKCi4-7OC2KBhY"
        res = urllib.request.urlopen(url)
        data = json.load(res)
        subs = data['items'][0]['statistics']['subscriberCount']
    except:
        subs='cant load'
    msg_to_show = msg + subs

    # Start The Display
    print(msg_to_show)
    while(True):
        show_message(device, msg_to_show, fill="white", font=proportional(CP437_FONT))
        time.sleep(1)

if __name__ == "__main__":
    try:
        demo()
    except KeyboardInterrupt:
        pass
