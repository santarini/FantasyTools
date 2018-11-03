#import schedule

import requests
from bs4 import BeautifulSoup as bs
import time
import csv

response = requests.get('https://www.basketball-reference.com/players/j/jamesle01/gamelog/2018/')
soup = bs(response.text, 'lxml')

playerDataTable = soup.find("table", {"id": "pgl_basic"})

with open('myPlayer.csv', 'a') as csvfile:
    fieldnames = ["Season Game",
                  "Date",
                  "Opponent",
                  "Minutes Played",
                  "FG",
                  "FGA",
                  "3P",
                  "3A",
                  "FT",
                  "FTA",
                  "TRB",
                  "AST",
                  "STL",
                  "BLK",
                  "TOV",
                  "PTS"
                  ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
    writer.writeheader()
    
    for tableRow in playerDataTable.findAll('tr')[1:]:
        try: 
            if "thead" in tableRow.get('class'):
                continue
        except TypeError:
            rank = (tableRow.findAll('td')[0])
            date = (tableRow.findAll('td')[1])
            opponent = (tableRow.findAll('td')[5])
            minsPlayed = (tableRow.findAll('td')[8])
            fgm = (tableRow.findAll('td')[9])
            fga = (tableRow.findAll('td')[10])
            threePt = (tableRow.findAll('td')[12])
            threePtAtm = (tableRow.findAll('td')[13])
            freeThrow =(tableRow.findAll('td')[15])
            freeThrowAtm =(tableRow.findAll('td')[16])
            reb =(tableRow.findAll('td')[20])
            assts =(tableRow.findAll('td')[21])
            stls = (tableRow.findAll('td')[22])
            blcks = (tableRow.findAll('td')[23])
            turnOvs = (tableRow.findAll('td')[24])
            pts = (tableRow.findAll('td')[26])
        
            writer.writerow({
                "Season Game":rank.text,
                "Date":date.text,
                "Opponent":opponent.text,
                "Minutes Played":minsPlayed.text,
                "FG":fgm.text,
                "FGA":fga.text,
                "3P":threePt.text,
                "3A":threePtAtm.text,
                "FT":freeThrow.text,
                "FTA":freeThrowAtm.text,
                "TRB":reb.text,
                "AST":assts.text,
                "STL":stls.text,
                "BLK":blcks.text,
                "TOV":turnOvs.text,
                "PTS":pts.text
                })
            



#8th table : <table class="row_summable sortable stats_table" data-cols-to-freeze="3" id="pgl_basic">

# Skip trs with class thead <tr class="thead">
