#import schedule

import requests
from bs4 import BeautifulSoup as bs
import time


response = requests.get('https://www.basketball-reference.com/players/j/jamesle01/gamelog/2018/')
soup = bs(response.text, 'lxml')

x = 0
for table in soup.findAll("table"):
    x +=1
    print("\n\n======================== " + str(x) + "========================\n\n")
    print(table)

#8th table : <table class="row_summable sortable stats_table" data-cols-to-freeze="3" id="pgl_basic">
