class Painting:
    def __init__(self,paintingID , painterName,paintingPrice,paintingtype):
        self.paintingID = paintingID
        self.painterName = painterName
        self.paintingPrice = paintingPrice
        self.paintingtype = paintingtype
        

class ShowRoom:
    
    def getTotalPaintingPrice(self, paintingList,painting_type):
        result = []
        for i in paintingList:
            if painting_type == i.paintingtype:
                result.append(i.paintingPrice)
            else:
                None
             
        return result
    def getPianterWithMaxCountOfPaintings(self , paintingList):
        max_painting = 0
        max_name = []
        
    #  incomplete coded
            
                
         
    

if __name__ == '__main__':
    
    n = int(input())
    # for loop
    paintingList = []
    for i in range(n):
        paintingID = input()
        painterName = input()
        paintingPrice = int(input())
        paintingtype = input()
        
        paintingList.append(Painting(paintingID,painterName,paintingPrice,paintingtype))

painting_type = input()