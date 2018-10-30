# Fantasy Tools

Our fantasy basketball league moved from ESPN to Yahoo. Yahoo doesn't seem to offer as much data on players as ESPN did. One of the missing metrics that I found to be of particular importantance in determining ideal fantasy lineups was the number of games scheduled for each player each week. Manually finding this number for each player has proven very tedious.

YahooBballFantasy.py logs into your Yahoo account team page and scrapes your team's info to a CSB.
Scheduler.py reads the team names from the CSVs and creates a CSV # of games for that respective week.
Having this information should provide a significant advantage over lesser informed leaguemates.

### Yahoo team games per week and pts projection

- [x] Login to yahoo league page
- [x] Scrape player data, team, and pos
- [X] Export player, team, pos to CSV
- [X] Search for resource that lists team scheudle by week
- [X] Use resource to find games per week
- [X] Export games per week to CSV by player
- [ ] Combine yahoo scrape and scheduler into functions in single py file
- [ ] Figure out method for projecting pts per week
- [ ] Create algoritim for determining which week of regular season it is

### Yahoo free agent games per week and pts projection

- [ ] Login to yahoo league page
- [ ] Navigate to free agency list
- [ ] Scrape player data, team, and pos
- [ ] Export player, team, pos to CSV

### Yahoo opponent games per week and pts projection

- [ ] Login to yahoo league page
- [ ] Navigate to each leaguemate's team
- [ ] Scrape player data, team, and pos
- [ ] Export player, team, pos to CSV
