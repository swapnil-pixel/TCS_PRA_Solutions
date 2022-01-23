class Medicine:
    
    def __init__(self,MedicineName,batch,disease,price):
        self.MedicineName = MedicineName
        self.batch = batch
        self.disease = disease
        self.price = price
        
class Solution:
    
    @staticmethod
    def getPriceByDisease(list_medicine,disease):
        result = []
        
        for i in list_medicine:
            if i.disease.lower() == disease.lower():
                result.append(i.price)
                
        return result
    
if __name__ == '__main__':  
           
    n = int(input())
    list_medicine = []
    for i in range(n):
        
        medicineName = input()
        batch = input()
        disease = input()   
        price = int(input())  
        
        list_medicine.append(Medicine(medicineName,batch,disease,price))
        
        
    disease = input()
    answer = Solution.getPriceByDisease(list_medicine,disease)

    for i in range(answer):
        print(answer[i])
        
    