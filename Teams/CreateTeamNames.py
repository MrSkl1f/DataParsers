import urllib.request, urllib.parse, urllib.error
import json

MAX_N = 100
needSport = "Soccer"

def checkData(data):
    if  data['strTeam'] != '' and data['strTeam'] != None and\
        data['strCountry'] != '' and data['strCountry'] != None and data['strCountry'] != 'International' and\
        data['strStadium'] != '' and data['strStadium'] != None:
            return True
    return False

def save(team):
    f = open("Team.csv", "w", encoding='utf-8')
    for i in range(MAX_N):
        print(team[i])
        teamID          = str(i + 1)
        teamName        = team[i][0]
        country         = team[i][2]
        stadium         = team[i][1]

        line =  teamID       + ',' +\
                teamName    + ',' +\
                country     + ',' +\
                stadium     + '\n'
        f.write(line)
    f.close()

def createTeam():
    urlForLeagues = 'https://www.thesportsdb.com/api/v1/json/1/all_leagues.php'
    leaguesData = urllib.request.urlopen(urlForLeagues).read().decode()
    leaguesData = json.loads(leaguesData)
    sumAll = sum([1 for item in leaguesData['leagues']])
    team = []
    check = 0
    for i in range(sumAll):
        if leaguesData['leagues'][i]['strSport'] == needSport:
            urlForTeamsInLeague = 'https://www.thesportsdb.com/api/v1/json/1/lookup_all_teams.php?id=' + str(leaguesData['leagues'][i]['idLeague'])
            teamsData = urllib.request.urlopen(urlForTeamsInLeague).read().decode()
            teamsData = json.loads(teamsData)
            if teamsData['teams'] != None:
                arr = [1 for item in teamsData['teams']]
                sumAll2 = sum(arr)
                for j in range(sumAll2):
                    if (len(team) < MAX_N):
                        if checkData(teamsData['teams'][j]):
                            country = teamsData['teams'][j]['strCountry'].split('\t')
                            team.append([teamsData['teams'][j]['strTeam'], teamsData['teams'][j]['strStadium'], country[0]])
                    else:
                        check = 1
                        break
        if check:
            break
    return team
team = createTeam()
#save(team)
    