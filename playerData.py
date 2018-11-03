#import schedule

import requests
from bs4 import BeautifulSoup as bs
import time


response = requests.get('https://www.basketball-reference.com/players/j/jamesle01/gamelog/2018/')
soup = bs(response.text, 'lxml')

x = 0

playerDataTable = soup.find("table", {"id": "pgl_basic"})
for tableRow in playerDataTable.findAll('tr'):
    try: 
        if "thead" in tableRow.get('class'):
            continue
    except TypeError:
        for row in tableRow:
            print(row)
print(x)



#8th table : <table class="row_summable sortable stats_table" data-cols-to-freeze="3" id="pgl_basic">

# Skip trs with class thead <tr class="thead">
