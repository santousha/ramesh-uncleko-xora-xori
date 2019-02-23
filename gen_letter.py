
import string

letters = list(string.ascii_uppercase)


def gen_boys():
    for l in letters:
        loot_boy = {
        'letter' : l,
        'url': f'http://www.easynepalityping.com/resource_dynamic/babynames/nepal/nepalBoy{l}.html',
        'file' :  f'boy_{l}.html'
        }
        yield loot_boy

def gen_girls():
    for l in letters:
        loot_girl =  {
        'letter' : l,
        'url':  f'http://www.easynepalityping.com/resource_dynamic/babynames/nepal/nepalGirl{l}.html',
        'file' : f'girl_{l}.html'
        }
        yield loot_girl