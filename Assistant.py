
import os
import json
import datetime

from bot import Bot

class Assistant(Bot):
    
    __PATH = os.getcwd()
    __BOT = 'bot.json'
    __SCHEDULE = 'schedule.txt'
    
    def __init__(self):
        super().__init__()
        self.initialize()
    
    def run(self):
        pass
    
    def initialize(self):
        
        print("Initialize ...")
        for file in os.listdir(self.__PATH):
            if file == self.__BOT:
                super().bot_init(path=os.path.join(self.__PATH, self.__BOT))
                print("Initialize completed!")
                print(f"Hello {self.get_user()}, {self.get_bot_name()} here. How can I help ?")
                break
        else:
            print(f"Hi, this is the first time we meet. My name Jarvis")
            print("What is your name? ")
            user = input("Your name: ")
            self.bot_init(path=self.__BOT, user=user)
            print(f"Hello {self.get_user()}, {self.get_bot_name()} here. How can I help ?")
        
    def create_schedule(self):
        pass
    
    def show_schedule(self):
        pass
    
    def throw_jokes(self):
        pass
    
    def send_email(self):
        pass
    
    
    def bot_init(self, path, user, name='Jarvis'):
        
        with open(path, 'w') as bot:
            self.set_bot(name)
            self.set_born(str(datetime.datetime.now()))
            self.set_user(user)
            json.dump(super().__dict__, bot)

