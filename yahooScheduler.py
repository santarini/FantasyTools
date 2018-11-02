#import schedule
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import csv
from datetime import datetime, timedelta

NBACalendarList = [
    ["2018-10-15",1],
    ["2018-10-22",2],
    ["2018-10-29",3],
    ["2018-11-05",4],
    ["2018-11-12",5],
    ["2018-11-19",6],
    ["2018-11-26",7],
    ["2018-12-03",8],
    ["2018-12-10",9],
    ["2018-12-17",10],
    ["2018-12-24",11],
    ["2018-12-31",12],
    ["2019-01-07",13],
    ["2019-01-14",14],
    ["2019-01-21",15],
    ["2019-01-28",16],
    ["2019-02-04",17],
    ["2019-02-11",18],
    ["2019-02-18",19],
    ["2019-02-25",20],
    ["2019-03-04",21],
    ["2019-03-11",22],
    ["2019-03-18",23],
    ["2019-03-25",24],
    ["2019-04-01",25],
    ["2019-04-08",26]
]

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

#def DayOfTheWeek():                
#figure out today and figure out when the first day of this week
today = datetime.today().weekday()
beginWeek = datetime.today() - timedelta(days=(today)) #if week starts with Mon: days=today, if week starts with Sun: days=today+1

#make a list of each day this week

datesInWeek =[]

for x in range (0, 7):
    datesInWeek.append((beginWeek + timedelta(days = x)).strftime('%Y-%m-%d'))

#figure out what week it is
for x in range(0, len(NBACalendarList)):
    if any(y == NBACalendarList[x][0] for y in datesInWeek):
        thisWeek = NBACalendarList[x][1]


def GetMyTeamData():
    #surfacebook and work computer webdriver path
    driver = webdriver.Firefox()

    #driver.set_window_size(1600, 1600)
    driver.set_window_position(0, 0)
    driver.get('https://basketball.fantasysports.yahoo.com/nba/157752/7')

    time.sleep(1)

    loginField = driver.find_element_by_id('login-username')
    loginField.send_keys('eventh')
    loginButton = driver.find_element_by_id('login-signin')
    loginButton.click()

    time.sleep(3)

    passField = driver.find_element_by_id('login-passwd')
    passField.send_keys('JpVWzUU5gEaApiy')
    passButton = driver.find_element_by_id('login-signin')
    passButton.click()

    time.sleep(3)

    statTable = driver.find_element_by_id('statTable0').get_attribute('innerHTML')
    statTable = statTable.encode('utf-8')
    teamTable = bs(statTable, 'lxml')

    tableBody = teamTable.find("tbody")

    with open('myTeam.csv', 'a') as csvfile:
        fieldnames = ['Player',
                      'Team',
                      'Position'
                      ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()

        for row in tableBody.findAll("tr"):
            player = row.findAll("a")[1].text
            teamAndPos = row.findAll("span")[3].text
            team = teamAndPos.split(" - ", 1)[0]
            pos = teamAndPos.split(" - ", 1)[1]
            writer.writerow({'Player': player,
                             #'Team': teamDict["Atl"][0],
                             'Team': team,
                             'Position': pos
                             })
        
    driver.quit()

def GetTeamSchedule(weekNo=thisWeek):
    teamSchedule = []

    #get schedule data
    response = requests.get('https://basketballmonster.com/ScheduleGrid.aspx')
    soup = bs(response.text, 'lxml')

    #find table
    dataTable = soup.find('table')

    #team row
    teamRow = dataTable.findAll('tr')[3]

    #get number of games this week by team
    weekRow = dataTable.findAll('tr')[3 + weekNo]

    for row in weekRow.findAll('td')[4:]:
        teamSchedule.append(row.text)

    with open('thisWeek.csv', 'a') as csvfile:
        fieldnames = ['Player',
                      'Team',
                      'Position',
                      'Games'
                      ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()

        with open("myTeam.csv") as csvfile:
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





    
