import requests
from bs4 import BeautifulSoup as bs
import csv

teamDict = {
    "Atl": ["ATL", 0], 
    "Bkn": ["BKN", 1],	
    "Bos": ["BOS", 2],	
    "Cha": ["CHA", 3],
    "Chi": ["CHI", 4],	
    "Cle": ["CLE", 5],	
    "Dal": ["DAL", 6],	
    "Den": ["DEN", 7],	
    "Det": ["DET", 8],	
    "GS": ["GSW", 9],	
    "Hou": ["HOU", 10],	
    "Ind": ["IND", 11],
    "LAC": ["LAC", 12],	
    "LAL": ["LAL", 13],	
    "Mem": ["MEM", 14],	
    "Mia": ["MIA", 15],	
    "Mil": ["MIL", 16],
    "Min": ["MIN", 17],	
    "NO": ["NOR", 18],	
    "NY": ["NYK", 19],	
    "OKC": ["OKC", 20],	
    "Orl": ["ORL", 21],	
    "Phi": ["PHI", 22],	
    "Pho": ["PHO", 23],	
    "Por": ["POR", 24],	
    "Sac": ["SAC", 25],	
    "SA": ["SAS", 26],	
    "Tor": ["TOR", 27],	
    "Uta": ["UTA", 28],	
    "Was": ["WAS", 29]
    }

teamSchedule = []

#get schedule data
response = requests.get('https://basketballmonster.com/ScheduleGrid.aspx')
soup = bs(response.text, 'lxml')

#find table
dataTable = soup.find('table')

#team row
teamRow = dataTable.findAll('tr')[3]

#set week no
#hint: week 1 = 4th tr
weekNo = 3

#get number of games this week by team
weekRow = dataTable.findAll('tr')[3 + weekNo]

for row in weekRow.findAll('td')[4:]:
    teamSchedule.append(row.text)

with open('thisweek.csv', 'a') as csvfile:
    fieldnames = ['Player',
                  'Team',
                  'Position',
                  'Games'
                  ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
    writer.writeheader()

    with open("players.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player = (row['Player'])
            team = (row['Team'])
            position = (row['Position'])

            #reference team name with teamSchedule index number
            #get number from teamScheudle
            gamesScehduled = teamDict[team][1]

            #write number to CSV
            writer.writerow({'Player': player,
                             'Team': team,
                             'Position': position,
                             'Games': teamSchedule[gamesScehduled]
                             })
