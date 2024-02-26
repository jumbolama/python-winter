# oop.py

class Burger:

    def bun(self):
        print('bun')
        return self
    
    def patty(self):
        print('patty')
        return self
    
    def cheese(self):
        print('cheese')
        return self
    
burger=Burger()

burger.bun().patty().cheese().bun()