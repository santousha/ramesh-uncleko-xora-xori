
# Data yesto xa.. majale lutne ho muji

# http://www.easynepalityping.com/resource_dynamic/babynames/nepal/nepalBoyC.html
# http://www.easynepalityping.com/resource_dynamic/babynames/nepal/nepalGirlK.html

import requests

import string
from pathlib import Path


letters = list(string.ascii_uppercase)
save_dir = Path.cwd().joinpath("luteko-data")

for l in letters:
    loot_boy = {
        'url': f'http://www.easynepalityping.com/resource_dynamic/babynames/nepal/nepalBoy{l}.html',
        'file' : f'boy_{l}.html'
        }
    loot_girl =  {
        'url':  f'http://www.easynepalityping.com/resource_dynamic/babynames/nepal/nepalGirl{l}.html',
        'file' : f'girl_{l}.html'
        }
    print ( f"Getting File: {loot_boy.get('file')}" )
    r1 = requests.get(loot_boy.get('url'), allow_redirects=True)
    print ( f"Getting File: {loot_girl.get('file')}" )
    r2 = requests.get(loot_girl.get('url'), allow_redirects=True)

    f1 = save_dir.joinpath(loot_boy.get('file'))
    f2 = save_dir.joinpath(loot_girl.get('file'))
    open(f1, 'wb').write(r1.content)
    open(f2, 'wb').write(r2.content)
    