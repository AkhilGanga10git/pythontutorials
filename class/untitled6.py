class Baseclass:
    def setname(self,name):        
        self.name=name

        
        
class subclass(Baseclass):
    def welcome(self):
        print('welcome')
    def dsiplayname(self):
        print(+name)
        

x=Baseclass()
y=subclass()
y.setname("aa")
y.welcome()

