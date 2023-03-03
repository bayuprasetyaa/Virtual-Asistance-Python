
import os
import json
import datetime
import urllib

from bot import Bot

class Assistant(Bot):
    
    def __init__(self):
        super().__init__()
        self.initialize()
            
    def initialize(self):
        print("Initialize ...")
        if self.valid(self.get_BOT()):
            super().bot_init(path=os.path.join(self.get_PATH(), self.get_BOT()))
            print("Initialize completed!")
        else:
            print(f"Hi, this is the first time we meet. My name Jarvis")
            print("What is your name? ")
            user = input("Your name: ")
            self.bot_init(path=self.get_BOT(), user=user)
            
        
    def create_schedule(self, date, agenda):
        if self.valid(self.get_SCHEDULE()):
            with open(self.get_SCHEDULE(), 'a') as file:
                file.write(f"{date} - {agenda}")
        else:
            with open(self.get_SCHEDULE(), 'w') as file:
                file.write(f"\n{date} - {agenda}")
        
        print("Schedule created !")
    
    def show_schedule(self):
        if self.valid(self.get_SCHEDULE()):
            with open(self.get_SCHEDULE(), 'r') as file:
                return file.read()
    
    def throw_jokes(self):
        
        new_joke = self.search_joke()
        
        if self.valid(self.get_JOKE()):
            with open(self.get_JOKE(), 'a') as file:
                file.write(f"\n{new_joke}")
            return open(self.get_JOKE(), 'r').read()
        elif len(new_joke) > 0:
             with open(self.get_JOKE(), 'w') as file:
                file.write(f"{new_joke}")
             return open(self.get_JOKE(), 'r').read()
        else:
            return "No Joke"
    
    def send_email(self):
        pass
    
    def shut_down(self):
        print(f"Good Bye {self.get_user()} !")
        exit()
    
    
    # Validation method
    def valid(self, check_file):
        
        for file in os.listdir(self.get_PATH()):
            if file == check_file:
                return True
        else:
            return False
    
    def bot_init(self, path, user, name='Jarvis'):
        
        with open(path, 'w') as bot:
            self.set_bot(name)
            self.set_born(str(datetime.datetime.now()))
            self.set_user(user)
            json.dump(super().__dict__, bot)

