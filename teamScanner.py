#import schedule
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import csv
from datetime import datetime, timedelta
import os

#create source folder if it doesnt exist yet
if not os.path.exists('opponentTeams'):
    os.makedirs('opponentTeams')


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

#i'm number 7 so skip num 7
for x in [i for i in range(1,9) if i!=7]:
    driver.get('https://basketball.fantasysports.yahoo.com/nba/157752/' + str(x))

    #get teamName
    
    teamCard = driver.find_element_by_id('team-card-info').get_attribute('innerHTML')
    teamCard = teamCard.encode('utf-8')
    teamCard = bs(teamCard, 'lxml')
    teamName = teamCard.findAll("a")[0].text
    teamName = teamName.split("  ")[0]

    #encode teamName for CSV file name --> teamName.replace(" ", "").replace("'", "")
    fileName = teamName.replace(" ", "").replace("'", "")

    #get player data
    statTable = driver.find_element_by_id('statTable0').get_attribute('innerHTML')
    statTable = statTable.encode('utf-8')
    teamTable = bs(statTable, 'lxml')

    tableBody = teamTable.find("tbody")
    if not os.path.exists('opponentTeams/' + fileName + '.csv'):
        print("Getting " + teamName)
        with open('opponentTeams/' + fileName + '.csv', 'a') as csvfile:
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
    else:
        print("Already have " + teamName)

print('Done.')
driver.quit()
