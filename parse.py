
from pathlib import Path
import re
import json

from bs4 import BeautifulSoup as Soup
from gen_letter import *

# Niwwa dont fuckin ask what this whole shit does

name_regex = r"&&(.*?)&&"
html_dir = Path.cwd().joinpath("luteko-data")
fname_dir = Path.cwd().joinpath("first-names")

def extract_name(name):
    matches = re.search(name_regex, name)
    if matches:
        return matches.group(1)

def parser_black_magic(gen_list, save_name):
    # The dictionary
    shit_dict = dict()
    for entry in gen_list:
        ltr = entry.get('letter')
        html =  html_dir.joinpath(entry.get('file'))
        conts = open(html, mode="r", encoding="utf-8")
        soup = Soup(conts.read(), "html5lib")
        links = soup.find_all('a')
        names_raw = [n.get('name') for n in links if n.get('name') is not None ]
        names = [extract_name(n) for n in names_raw]
        shit_dict[ltr] = names
    # RAM ? Its free real estate
    with open(fname_dir.joinpath(save_name), "w",  encoding="utf-8") as f:
        json.dump(shit_dict, f, sort_keys=True, indent=2)

parser_black_magic(gen_boys(), "b.json")
parser_black_magic(gen_girls(), "g.json")