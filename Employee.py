class employee:
    def __init__(self,emp_Id , emp_name,emp_role,emp_salary):
        self.emp_Id = emp_Id
        self.emp_name = emp_name
        self.emp_role = emp_role
        self.emp_salary = emp_salary
        
        
    def increment_salary(self,percentage):
        self.emp_salary = self.emp_salary + (self.emp_salary * percentage/100)
    
class organization:
    def __init__(self,org_name,emp_obj):
            self.org_name = org_name
            self.emp_obj = emp_obj  
            
    def calculate_salary(self,emp_role_,percentage , emp_obj):
        self.emp_role_ = emp_role_  
        self.percentage = percentage    
        emp_list =[]
        for i in emp_obj:
            if(i.emp_role == emp_role_):
                i.increment_salary(percentage)
                emp_list.append(i)
        return emp_list
        
        
        
if __name__ == '__main__':
    
    n= int(input())
    emp_obj = []
    for i in range(n):
        emp_Id = int(input("Enter ID:"))
        emp_name = input("Enter name:")
        emp_role = input("Enter role:")
        emp_salary = int(input("Enter salary:"))
        
    
        # emp object created
        emp_obj.append(employee(emp_Id,emp_name,emp_role,emp_salary))
    org = organization("ABC",emp_obj) 
    emp_role_ = input()
    percentage = int(input("Enter the percentage by which salary increase"))
    result = org.calculate_salary(emp_role_,percentage, emp_obj)
    for i in result:
        print(i.emp_name)
        print(i.emp_salary)
        
     
