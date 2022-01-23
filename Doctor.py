class Doctor:
    
    def __init__(self,doctorId,doctorName,Specialization,consultationFee):
        self.doctorId = doctorId
        self.doctorName = doctorName
        self.Specialization = Specialization
        self.consultationFee = consultationFee
        
class Hospital:
    
    def __init__(self, doctorDB, doctorName_searchFor):
        self.doctorDB = doctorDB
        self.doctorName_searchFor = doctorName_searchFor
        
        
        
        
        
if __name__ == '__main__':
    n = int(input())
    doctorDB = {}
    for i in range(n):
        doctorId = int(input())
        doctorName = input()
        Specialization = input()
        consultationFee = int(input())
        
        doctorobj = Doctor(doctorId,doctorName,Specialization,consultationFee)
        doctorDB.update({i:doctorobj})
        doctorName_searchFor = input()
        
    
