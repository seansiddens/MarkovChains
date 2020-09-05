import random
import json
import argparse


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
            if i + 1 < len(phrase):
                words[phrase[i]].append(phrase[i+1])
            else:
                continue
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


def generate_sentence(markov, start_word, count=100):
    current_state = start_word
    word_count = 1

    while next_word(current_state, markov) != -1 and word_count < count:
        print(current_state, end=' ')
        next_state = next_word(current_state, markov)
        word_count += 1
        current_state = next_state


def load_data(file_name='data.txt'):
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


def get_metadata(data_file):
    with open(data_file, 'r') as f:
        for line in f:
            yield line


def create_abstract_data(input_name, output_name):
    data_file = input_name

    metadata = get_metadata(data_file)
    f = open(output_name, 'w', encoding='utf8')

    for paper in metadata:
        paper_dict = json.loads(paper)
        abstract = paper_dict.get('abstract')
        f.write(abstract)

    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--data", '-d', help="Data file used to train Markov Chain")
    parser.add_argument("--number", '-n', help="Number of words to generate")
    parser.add_argument("--word", '-w', help="Set starting word")
    args = parser.parse_args()

    if args.data:
        markov_chain = create_markov_chain(load_data(args.data))
    else:
        markov_chain = create_markov_chain(load_data())

    if args.number and args.word:
        generate_sentence(markov_chain, args.word, int(args.number))
    elif args.word:
        generate_sentence(markov_chain, args.word)






