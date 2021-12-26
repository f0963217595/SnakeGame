import random
class Apple:
    #建構方法:初始值設定用
    def __init__(self):
        self.x = random.randint(0,79) * 10
        self.y = random.randint(0,59) * 10
        self.onScreen = True

    def createApple(self):
        if self.onScreen == False:
            self.x = random.randint(0,79) * 10
            self.y = random.randint(0,59) * 10
            self.onScreen = True
    def changeStatus(self, status):
        self.onScreen = status
