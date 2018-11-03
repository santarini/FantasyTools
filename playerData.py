#import schedule

import requests
from bs4 import BeautifulSoup as bs
import time
import csv

response = requests.get('https://www.basketball-reference.com/players/j/jamesle01/gamelog/2017/')
soup = bs(response.text, 'lxml')

playerDataTable = soup.find('table', {'id': 'pgl_basic'})
playerDataTableBody = playerDataTable.find('tbody')


with open('myPlayer.csv', 'a') as csvfile:
    fieldnames = ["Season Game",
                  "Date",
                  "Team",
                  "at",
                  "Opponent",
                  "winLoss",
                  "Seconds Played",
                  "FG",
                  "FGA",
                  "FG%",
                  "3P",
                  "3A",
                  "3%",
                  "FT",
                  "FTA",
                  "FT%",
                  "TRB",
                  "AST",
                  "STL",
                  "BLK",
                  "TOV",
                  "PF",
                  "PTS"
                  ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
    writer.writeheader()

    for tableRow in playerDataTableBody.findAll('tr'):
        if tableRow.has_attr('class'):
            print('Header')
            continue
        if tableRow.findAll('td')[7].get('data-stat') == 'reason':
            print('Reason')
        else:
            rank = tableRow.find('th', {'data-stat' : 'ranker'})
            date = tableRow.find('td', {'data-stat' : 'date_game'})
            team = tableRow.find('td', {'data-stat' : 'team_id'})
            at = tableRow.find('td', {'data-stat' : 'game_location'})         
            opponent = tableRow.find('td', {'data-stat' : 'opp_id'}) 
            winLoss = tableRow.find('td', {'data-stat' : 'game_result'}).get('csk')   
            secsPlayed = tableRow.find('td', {'data-stat' : 'mp'}).get('csk')
            fgm = tableRow.find('td', {'data-stat' : 'fg'})
            fga = tableRow.find('td', {'data-stat' : 'fga'})
            fgPercent = tableRow.find('td', {'data-stat' : 'fg_pct'})
            threePt = tableRow.find('td', {'data-stat' : 'fg3'})
            threePtAtm = tableRow.find('td', {'data-stat' : 'fg3a'})
            threePercent = tableRow.find('td', {'data-stat' : 'fg3_pct'})
            freeThrow = tableRow.find('td', {'data-stat' : 'ft'})
            freeThrowAtm = tableRow.find('td', {'data-stat' : 'fta'})
            freeThrowPercent = tableRow.find('td', {'data-stat' : 'ft_pct'})
            reb = tableRow.find('td', {'data-stat' : 'trb'})
            assts = tableRow.find('td', {'data-stat' : 'ast'})
            stls = tableRow.find('td', {'data-stat' : 'stl'})
            blcks = tableRow.find('td', {'data-stat' : 'blk'})
            turnOvs = tableRow.find('td', {'data-stat' : 'tov'})
            personalFouls = tableRow.find('td', {'data-stat' : 'pf'})
            pts = tableRow.find('td', {'data-stat' : 'pts'})

            writer.writerow({
                "Season Game":rank.text,
                "Date":date.text,
                "Team": team.text,
                "at": at.text,
                "Opponent":opponent.text,
                "winLoss": winLoss,
                "Seconds Played":secsPlayed,
                "FG":fgm.text,
                "FGA":fga.text,
                "FG%": fgPercent.text,
                "3P":threePt.text,
                "3A":threePtAtm.text,
                "3%":threePercent.text,
                "FT":freeThrow.text,
                "FTA":freeThrowAtm.text,
                "FT%":freeThrowPercent.text,
                "TRB":reb.text,
                "AST":assts.text,
                "STL":stls.text,
                "BLK":blcks.text,
                "TOV":turnOvs.text,
                "PF": personalFouls.text,
                "PTS":pts.text
                })
