#import schedule
import time
import datetime
import re
import random
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from bs4 import BeautifulSoup as bs
import os
import img2pdf
import schedule


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

time.sleep(2)

passField = driver.find_element_by_id('login-passwd')
passField.send_keys('1JpVWzUU5gEaApiy!')
passButton = driver.find_element_by_id('login-signin')
passButton.click()

time.sleep(3)

statTable = driver.find_element_by_id('statTable0').get_attribute('innerHTML')
statTable = statTable.encode('utf-8')
teamTable = bs(statTable, 'lxml')

tableBody = teamTable.find("tbody")

for row in tableBody.findAll("tr"):
    print(row.findAll("a")[1].text)
    teamAndPos = row.findAll("span")[3].text
    team = teamAndPos.split(" - ", 1)[0]
    pos = teamAndPos.split(" - ", 1)[1]
    print(team)
    print(pos)
    
#driver.quit()


