class mysampleclass:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        
        


    def add_age(self):
        
       self.age=self.age+1
    
    def relocate(self,place):
        self.place=place
    
    
    def display (self):
        print(self.name)
        print(self.age)
        print(self.place)
        
x=mysampleclass("akhil",25,"tvm")
y=mysampleclass("amal",15,"tvm")       
        
x.add_age()
y.add_age()

x.display()
y.display()