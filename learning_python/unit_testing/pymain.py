#! /usr/local/bin/python3

def textStuff():
    initdata = ['picard', 'kirk', 'Picard', 'archer', 'janeway', 'picard', 'archer']

    mr = {}
    for word in initdata:
        word = word.upper()
        if (word in mr):
            mr[word] += 1
        else:
            mr[word] = 1
    print(mr)

    print('----')

    reduced = {}
    mr2 = list(map(str.upper, initdata))
    for x in mr2:
        reduced[x] = mr2.count(x)
    print(reduced)

def doubleme(x):
    print(x * 2)
    return x * 2

if __name__ == "__main__":
    textStuff()