#import schedule

import requests
from bs4 import BeautifulSoup as bs
import time


response = requests.get('https://www.basketball-reference.com/players/j/jamesle01/gamelog/2018/')
soup = bs(response.text, 'lxml')

x = 0

playerDataTable = soup.find("table", {"id": "pgl_basic"})
for tableRow in playerDataTable.findAll('tr')[1:]:
    try: 
        if "thead" in tableRow.get('class'):
            continue
    except TypeError:
        rank = (tableRow.findAll('td')[0])
        date = (tableRow.findAll('td')[2])
        opponent = (tableRow.findAll('td')[6])
        minsPlayed = (tableRow.findAll('td')[9])
        fgm = (tableRow.findAll('td')[10])
        fga = (tableRow.findAll('td')[11])
        threePt = (tableRow.findAll('td')[13])
        thrrePtAtm = (tableRow.findAll('td')[14])
        freeThrow =(tableRow.findAll('td')[16])
        freeThrowAtm =(tableRow.findAll('td')[17])
        reb =(tableRow.findAll('td')[21])
        assts =(tableRow.findAll('td')[22])
        stls = (tableRow.findAll('td')[23])
        blcks = (tableRow.findAll('td')[24])
        turnOvs = (tableRow.findAll('td')[25])        

            



#8th table : <table class="row_summable sortable stats_table" data-cols-to-freeze="3" id="pgl_basic">

# Skip trs with class thead <tr class="thead">
