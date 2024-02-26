class grandfather:
    house='nice house'
    def __init__(self):
        print('how r u gdandy')

class father(grandfather):
    car='jeep'

    def __init__(self):
        print(self.car)

class mother:
    land='high prise land'

    def __init__(self):
        print(self.land)
        super().__init__()

class son(father,mother):
    game='ps5'


    def __init__(self):
        print(self.game)
        super().__init__()

Son=son()
#print(son.land,son.car)