import dice
class creature:
    
    def __init__(self, x):
        d = dice()
        self.hp = x[0]
        self.player = x[1]
        self.name = x[2]
        self.ac = x[3]
        self.flat = x[4]
        self.to_hit = x[5]
        self.fort = x[6]
        self.ref = x[7]
        self.will = x[8]
        self.order = d.d20()
        

    def __str__(self):
        s = "hp is : "+str(self.hp)
        s += "\n name is : "+str(self.name)
        s += "\n ac is : "+str(self.ac)            
        return s