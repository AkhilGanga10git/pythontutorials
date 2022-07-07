class mysample:
    def hello(self,n):
        self.name=n
    def print_name(self):
        print(self.name)

    
x=mysample()
y=mysample()
name="akhil"
x.hello(name)
y.hello("ganga2")
x.print_name()
y.print_name()