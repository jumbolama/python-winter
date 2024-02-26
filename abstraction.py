from abc import ABC,abstractmethod

class Computer(ABC):

    def run(self,app):
        self.process(app)

    @abstractmethod
    def process(self,app):
        pass

class Laptop(Computer):
    def process(self, app):
        print('Laptop is running on'+ app)

class Mobile(Computer):
    def process(self, app):
        print('Mobile is running on'+ app)

acer=Laptop()
acer.run('game')

samsung=Mobile()
samsung.run('google')