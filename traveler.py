#  This code is a ask ini the TCS IA exam 
# this code is written  by: Swapnil manoj patil

class Traveler:
    
    def __init__(self,travelerName,traveledCountry,travelerAge,countryfrom):
        self.travelerName = travelerName
        self.traveledCountry = traveledCountry
        self.travelerAge = travelerAge
        self.countryfrom = countryfrom


class TravelAgency:
    @classmethod
    def countTravelerTraveledCountry(cls,TravelerList , find_country):
        count = 0   #count = 0
        for i in TravelerList:
            if find_country in i.traveledCountry:
                count += 1
                
        return count

    @classmethod
    def getTravelerTravelledMaxCountry(cls,TravelerList):    #methos to return the travelername how travel max country
        max_conutry = 0
        max_name = "" 
        for i in TravelerList:
            list1 = i.traveledCountry
            if len(list1) > max_conutry:
                max_conutry = list1
                max_name = i.travelerName
                
        return max_name

# main 
    
if __name__ == "__main__":
    
    n = int(input())
    TravelerList= []
  
    for i in range(n):
        travelerName = input()
        c = int(input())    
        traveledCountry = []
        for j in range(c):
            traveledCountry.append(input())
           
            
        travelerAge = int(input())
        countryfrom = input()
        TravelerList.append(Traveler(travelerName,traveledCountry,travelerAge,countryfrom))
        
    find_country = input()
                
    ans_1 = TravelAgency.countTravelerTraveledCountry(TravelerList,find_country)
    ans_2 = TravelAgency.getTravelerTravelledMaxCountry(TravelerList)

    print(ans_1)
    print(ans_2)

