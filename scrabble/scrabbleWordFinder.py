#!/usr/bin/python3

from PIL import Image
from PIL import ImageFilter
import pytesseract #image parsing
from picamera import PiCamera
from time import sleep
import twl #scrabble dictionary
import PySimpleGUI as sg #UI

WORDS = set(twl.iterator())
LETTER_SCORES = {"a": 1, "b": 3, "c": 3, "d": 2,
                 "e": 1, "f": 4, "g": 2, "h": 4,
                 "i": 1, "j": 8, "k": 5, "l": 1,
                 "m": 3, "n": 1, "o": 1, "p": 3,
                 "q": 10, "r": 1, "s": 1, "t": 1,
                 "u": 1, "v": 4, "w": 4, "x": 8,
                 "y": 4, "z": 10}
starting_text = "X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0"

# UI
sg.theme('LightGrey1')
layout = [  [sg.Text('XXXXX', justification='center', key='letters', font=("Helvetica", 40))],
            [sg.Text('Top Word Scores:', justification='center', font=("Helvetica", 35))],
            [sg.Multiline(starting_text, size=(40, 20), key='words', font=("Helvetica", 15))],
            [sg.Button('Close', size=(8, 4))]
          ]
window = sg.Window('Scrabble Word Finder', layout, size=(820, 480), resizable=True)

def take_picture():
    loc = '/home/pi/scrabble/tiles.jpg'
    try:
        camera = PiCamera()
        print("Taking Picture...")
        camera.resolution = (1920, 600)
        camera.iso = 600
        camera.start_preview()
        sleep(1)
        camera.capture(loc)
        camera.stop_preview()
    finally:
        camera.close()
    return loc

def parse_picture(loc):
    print("Parsing Image...")
    img = Image.open (loc).convert('L')

    blackwhite = img.point(lambda x: 0 if x < 166 else 255, '1')
    blackwhite.save("tiles_bw.jpg")

    im = Image.open("tiles_bw.jpg")
    smooth_im = im.filter(ImageFilter.SMOOTH_MORE)

    text = pytesseract.image_to_string(smooth_im, config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 7')
    return text

def get_current_letters():
    loc = take_picture()
    letters = parse_picture(loc).lower()
    print("Letters Are: " + letters)
    letter_list = [x for x in letters]
    print(letter_list)
    if len(letter_list) < 1:
        return ['a', 'b', 'c', 'd']
    return letter_list


def get_scrabble_words():
    print("Getting Scrabble Dictionary...")
    return WORDS


def check_valid_words(current_tile_letters, scrabble_words):
    temp_word_array = []

    for word in scrabble_words:
        for letter in word:
            if letter not in current_tile_letters:
                break
            elif word.count(letter) > current_tile_letters.count(letter):
                break
        else:
            temp_word_array.append(word)
            continue
    temp_word_array.sort()
    return temp_word_array


def get_top_scoring_words(valid_words):
    word_and_score = dict()

    for word in valid_words:
        score = 0
        for letter in word:
            score += LETTER_SCORES.get(letter)
        word_and_score[word] = score

    return dict(sorted(word_and_score.items(), key=lambda x: x[1], reverse=True)[:10])


def start_scrabble():
    print("Loading Scrabble Word Finder...")
    scrabble_words = get_scrabble_words()  # scrabble dictionary

    while(True):
        event, values = window.read(timeout=100)

        current_tile_letters = get_current_letters()  # my tiles
        valid_words = check_valid_words(current_tile_letters, scrabble_words)
        top_word_scores = get_top_scoring_words(valid_words)


        letter_String = " ".join(str(x) for x in current_tile_letters)
        print(letter_String)
        window['letters'].update(letter_String)

        print("Top Word Scores:\n")
        print("\n".join("{}: {}".format(k, v) for k, v in top_word_scores.items()))
        window['words'].update("\n".join("{}: {}".format(k, v) for k, v in top_word_scores.items()))
        window.refresh()

        if event == sg.WIN_CLOSED or event == 'Close':	# if user closes window or clicks cancel
            break

    window.close()

if __name__ == '__main__':
    start_scrabble()
