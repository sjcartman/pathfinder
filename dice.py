import random
class dice:
    def __init__(self):
        self.data = []
    def d20(self):
        return random.randint(1,20)
    def d12(self):
        return random.randint(1,12)
    def d10(self):
        return random.randint(1,10)
    def d8(self):
        return random.randint(1,8)
    def d6(self):
        return random.randint(1,6)
    def d4(self):
        return random.randint(1,6)
   