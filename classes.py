class Sagar:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def greet(self):
        print("Hello, my name is " + self.name + " and my salary is " + str(self.salary))
    
s=Sagar("Raju",20000)
s.greet()
