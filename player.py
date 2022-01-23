class Player:
    
    def __init__(self,playerName,playedCountry,playerAge,countryFrom):
       self.playerName = playerName
       self.playedcountry = playedCountry
       self.playerAge = playerAge
       self.countryFrom = countryFrom
       
    
def countPlayers(playerList,country):
    count = 0
    for i in playerList:
        if country.lower() == i.countryFrom.lower():
            count += 1
            
    return count

def getplayerPlayedForMaxCountry(playerList):
    max_c = 0
    max_name = ''
    for i in playerList:
        if(len(i.playedCountry) > max_c):
            max_c = len(i.playedCountry)
            max_name = i.playerName
    
    return max_name
 

       
if __name__ == '__main__':
    
    n = int(input)
    playerList = []
    playedCountry = []
    playerName = input()
    
    c = int(input())
    
    for i in range(c):
        played_c = input()
        playedCountry.append(played_c)
        
    playerAge = int(input())
    countryFrom = input()
    
    playerList.append(Player(playerName,playedCountry,playerAge,countryFrom))
    
    country = input()
    
    countPlayers(playerList,country)
    getplayerPlayedForMaxCountry(playerList)
