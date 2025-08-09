
# Inheritance
class phone_version:
    
    def __init__(self):
        self.phone1=["keypad","basic version"]
        self.phone2="android"

    def phone1a(self):
        self.keys="new version"
        self.games="snake game"
        self.music="no"
    def phone2a(self):
        self.storage="minimum"
        self.privacy="basic"
        self.features="average"

class phone_version2(phone_version) :

    def phone1b(self):
        #phone_version.phone1a(self) this is also work 
        self.phone1a()
        self.keys1b="added buttons"
        self.games1b="we can install through blutooth"
        self.music1b="memory card facility"
        self.head_phones1b="head phones port"
    def display(self):
        print(self.keys,self.games,self.music)
        print(self.keys1b,self.games1b,self.music1b,self.head_phones1b)
        

customer=phone_version2()
customer.phone1b()
customer.display()


# multi-inheritance
class first_gen:
    def __init__(self):
        self.grandfather="ramaya"
        self.height="6ft"
        self.looks="gud"
        self.behaviour="funny"
        self.family ="9 mem"

class sec_gen(first_gen):
    def __init__(self):
        super().__init__() # call firstgen's constructor
        self.son="raghu"
        self.sheight="5.7 ft"
        self.slooks="ok"
        self.job="gov"
        self.kids="1 child"
        self.sfam="5 mem"

class third_gen(sec_gen):
    def __init__(self):
        super().__init__()
        self.name="ram"
        self.cbehaviour="funny"
        self.cheight="6 ft"
        
        
# create thirdgen object        
traits= third_gen()

# print all attribute
print(vars(traits))
































