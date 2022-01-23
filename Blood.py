class Blood:
    
    def __init__(self,BloodGroup,unitInHand):
        self.BloodGroup = BloodGroup
        self.unitInHand = unitInHand
        
        
class Bloodbank:
    
    def __init__(self,bloodList):
        self.bloodList = bloodList
        
    def isBloodAvailable(self,req_bloodGroup,req_unit):
        for i in self.bloodList:
            if i.BloodGroup == req_bloodGroup:
                if i.UnitInHand >= req_unit:
                    return "BloodAvailable"
                else:
                    return "Blood not Available"
    
    def findMinBloodStock(self):
        minBloodStock = self.bloodList[0].UnitInHand
        minBlood = self.bloodList[0].BloodGroup
        for i in range(1,len(self.bloodList)):
            if(self.bloodList[i].unitInHand < minBloodStock):
                minBloodStock = self.bloodList[i].unitInHand
                minBlood = self.bloodList[i].BloodGroup
                
        minBloodList = []
        
        for i in self.bloodList:
            if i.UnitInHand == minBloodStock:
                minBloodList.append(i.BloodGroup)
        return minBloodList
                
            
            
            
            
            
if __name__=='__main__':
    n = int(input())
    bloodList = []
    BloodGroup = input().upper()
    unitInHand = int(input())
    
    bloodList.append(Blood(BloodGroup,unitInHand))
    req_bloodGroup = input().upper()
    req_unit = int(input())
    
    
