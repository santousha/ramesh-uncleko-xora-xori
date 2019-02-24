from pathlib import Path
import re
import json

csv_dir = Path.cwd().joinpath("thar-data")
lname_dir = Path.cwd().joinpath("last-names")

import string

letters = list(string.ascii_uppercase)
save_name = 'l.json'

import pprint
from collections import deque

def trie(trie_ds, word):
    try:
        letter = word.popleft()
        out = trie(trie_ds.get(letter, {}), word)
    except IndexError:
        # End of the word
        return {}

    # Dont update if letter already present
    if not letter in trie_ds :
        trie_ds[letter] = out

    return trie_ds


def parser_black_magic():
    # The dictionary
    shit_dict = dict()
    csv =  csv_dir.joinpath('list.txt')
    conts = open(csv, mode="r", encoding="utf-8")
    trie_raw = {}
    pp = pprint.PrettyPrinter(indent=2)
    for line in conts:
        ltr = line[:1]
        name = line.rstrip('\n')
        trie_raw = trie(trie_raw, deque(name))
        shit_dict.setdefault(ltr, []).append(name)
    #shit_dict[ltr] = names
    pp.pprint(shit_dict)
    # RAM ? Its free real estate
    with open(lname_dir.joinpath(save_name), "w",  encoding="utf-8") as f:
        json.dump(shit_dict, f, sort_keys=True, indent=2)

parser_black_magic()