# Fantasy Tools

### Description

Our fantasy basketball league moved from ESPN to Yahoo. Yahoo doesn't seem to offer as much data on players as ESPN did (or maybe they do and I'm just too lazy to find it). One of the missing metrics that I found to be of particular importantance in determining ideal fantasy lineups was the number of games scheduled for each player each week. Manually finding this number for each player has proven very tedious. Having this information easily available should provide a significant advantage over lesser informed leaguemates (you'd think).

### Package Description

`YahooBballFantasy.py` logs into your Yahoo account team page and scrapes your team's info to a CSV.

`Scheduler.py` reads the team names from the CSVs and creates a CSV with # of games for that respective week.

`yahooScheduler.py` combines YahooBballFantasy.py and Scheduler.py into a single py file making each a function, so don't waste your time with them unless you're trying to do your own thing.

`teamScanner.py` creates CSVs for other leaguemates team.

Yes, I'm aware that these naming conventions are confusing.

# Main Process To-Do List

### Yahoo team games per week and pts projection

- [x] Login to yahoo league page
- [x] Scrape player data, team, and pos
- [X] Export player, team, pos to CSV
- [X] Search for resource that lists team scheudle by week
- [X] Use resource to find games per week
- [X] Export games per week to CSV by player
- [X] Combine yahoo scrape and scheduler into functions in single py file
- [ ] Figure out method for projecting pts per week
- [X] Create algoritim for determining which week of regular season it is
- [ ] Prompt user for which data they want
- [ ] Print respective week on CSV output
- [ ] Modify operation to use single CSV
- [ ] Go to "opponenet" tab and add schedule/oppnenet data to csv scrape


### Points estimation

- Look at all games player did last season
- Figure out seasonal totals and averages
- Look at averages and totals over careers looking for trends
- Look at averages and totals against team (home and away)
- Look at Vegas'point totals and figure out what % should be attributable to player

- [ ] Go to player basketball-reference page and pull last season's stats

# Other Ideas

### Yahoo free agent games per week and pts projection

- [ ] Login to yahoo league page
- [ ] Navigate to free agency list
- [ ] Scrape player data, team, and pos
- [ ] Export player, team, pos to CSV

### Yahoo opponent games per week and pts projection

- [X] Login to yahoo league page
- [X] Navigate to each leaguemate's team
- [X] Scrape player data, team, and pos
- [X] Export player, team, pos to CSV

https://www.basketball-reference.com/players/j/jamesle01/gamelog/2018/
