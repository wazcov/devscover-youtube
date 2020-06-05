import twl

TEST_LETTER_ARRAY = ['x', 'z', 'p', 't', 'p', 'l', 'i']
WORDS = set(twl.iterator())
LETTER_SCORES = {"a": 1, "b": 3, "c": 3, "d": 2,
                 "e": 1, "f": 4, "g": 2, "h": 4,
                 "i": 1, "j": 8, "k": 5, "l": 1,
                 "m": 3, "n": 1, "o": 1, "p": 3,
                 "q": 10, "r": 1, "s": 1, "t": 1,
                 "u": 1, "v": 4, "w": 4, "x": 8,
                 "y": 4, "z": 10}


def get_current_letters():
    return TEST_LETTER_ARRAY


def get_scrabble_words():
    # return ['apple', 'lemon', 'ape', 'at', 'cheese', 'eggs', 'cow']
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
    current_tile_letters = get_current_letters()  # my tiles
    scrabble_words = get_scrabble_words()  # scrabble dictionary

    valid_words = check_valid_words(current_tile_letters, scrabble_words)
    top_word_scores = get_top_scoring_words(valid_words)

    print("\n".join("{}: {}".format(k, v) for k, v in top_word_scores.items()))


if __name__ == '__main__':
    start_scrabble()
