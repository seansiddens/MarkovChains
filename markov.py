import urllib.request
import json

import random
import requests
from bs4 import BeautifulSoup as bs


def create_markov_chain(phrase):
    words = {}
    foo_dict = {}
    for i in range(len(phrase)):
        if phrase[i] not in words:
            words[phrase[i]] = []
            if i + 1 < len(phrase):
                words[phrase[i]].append(phrase[i+1])
            else:
                continue
            foo_dict[phrase[i]] = 1
        else:
            words[phrase[i]].append(phrase[i+1])

    return words


def next_word(word, markov):
    if word not in markov:
        return -1
    else:
        try:
            next_word_choice = random.choice(markov[word])
        except IndexError:
            next_word_choice = ''

    return next_word_choice


def generate_sentence(phrase, start_word, count):
    print(start_word, end=' ')
    markov_chain = create_markov_chain(phrase)
    current_state = start_word
    word_count = 1

    while next_word(current_state, markov_chain) != -1 and word_count < count:
        next_state = next_word(current_state, markov_chain)
        word_count += 1
        print(next_state, end=' ')
        current_state = next_state


def load_data(file_name):
    data = []
    try:
        f = open(file_name, "r", encoding='utf-8')
    except FileNotFoundError:
        print("Error in loading data: file '" + file_name + "' not found")
        exit(1)

    for line in f:
        line = line.split()
        data = data + line

    return data


if __name__ == "__main__":
    dataset = load_data("tom_sawyer.txt")

    generate_sentence(dataset, "The", 100)



