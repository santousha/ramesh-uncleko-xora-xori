
# Data yesto xa.. majale lutne ho muji

# http://www.easynepalityping.com/resource_dynamic/babynames/nepal/nepalBoyC.html
# http://www.easynepalityping.com/resource_dynamic/babynames/nepal/nepalGirlK.html



from pathlib import Path

import requests
from bs4 import BeautifulSoup as Soup

from gen_letter import *

save_dir = Path.cwd().joinpath("luteko-data")

for l in letters:


    print ( f"Getting File: {loot_boy.get('file')}" )
    r1 = requests.get(loot_boy.get('url'), allow_redirects=True)
    print ( f"Getting File: {loot_girl.get('file')}" )
    r2 = requests.get(loot_girl.get('url'), allow_redirects=True)

    s1 = Soup(r1.text, "html5lib").prettify()
    s2 = Soup(r2.text, "html5lib").prettify()
    f1 = save_dir.joinpath(loot_boy.get('file'))
    f2 = save_dir.joinpath(loot_girl.get('file'))
    open(f1, 'w', encoding="utf-8").write(s1)
    open(f2, 'w', encoding="utf-8").write(s2)
    