#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dict = {}
    infile = open(corpus)
    fulltext = infile.read()
    words = fulltext.split()
    key1=0
    key2=1
    value=2

    for count in range(len(words)-2):
        
        if (words[key1],words[key2]) in markov_dict:
            markov_dict[(words[key1],words[key2])] = markov_dict[(words[key1],words[key2])] + [words[value]]

        else:
            markov_dict[(words[key1],words[key2])] = [words[value]]
        key1 = key1 + 1
        key2 = key2 + 1
        value = value + 1
        

    return markov_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    allkeys = chains.keys()
    key = random.choice(allkeys)
    key1 = key[0]
    key2 = key[1]
    value = random.choice(chains[(key1, key2)])

    print key, key1, key2, value
    
    # for i in range(10):


    return "Here's some random text."


def main():
    print make_chains("foxbox.txt")
    print make_text(make_chains("foxbox.txt"))

    # args = sys.argv

    # # Change this to read input_text from a file
    # input_text = "Some text"

    # chain_dict = make_chains(input_text)
    # random_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()