from abc import ABC,abstractmethod

class Calcu(ABC):
    def run(self,num):
        self.process(num)

    @abstractmethod
    def process(self,num):
        pass

class add(Calcu):
    def process(self, num):
        print('add some num is'+ num) 

class sub(Calcu):
    def process(self, num):
        print(' some num is'+ num)        

Cash=add()
Cash.run('two')

Ton=sub()
Ton.run('one')