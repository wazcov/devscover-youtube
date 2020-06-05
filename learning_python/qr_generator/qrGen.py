#! /usr/local/bin/python3

import requests


rootURL = "https://chart.googleapis.com/chart?"


def gen_data():
    testdata = ["John", "Sarah", "Shelly"]
    return testdata


def create_qr():
    for i in gen_data():
        print(call_google(i))


def call_google(data):
    full_url = rootURL + "cht=qr&choe=UTF-8&" + "chs=256x256&" + "ch1=" + data
    r = requests.get(url=full_url)
    if r.status_code == 200:
        with open('./'+data+'.jpg', 'wb') as f:
            for chunk in r:
                f.write(chunk)


if __name__ == "__main__":
    create_qr()