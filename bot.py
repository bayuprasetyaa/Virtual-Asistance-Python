import os
import datetime
import json

class Bot:
    __PATH = os.getcwd()
    __BOT = 'bot.json'
    __SCHEDULE = 'schedule.txt'

    def __init__(self, name:str = None, born:datetime = None, user:str=None, log:str=None) -> None:
        """__init__

        Args:
            name (str): Bot name
            born (datetime): First time activate
        """
        
        self.__BOT_NAME = name
        self.__BORN = born
        self.__USER = user
        self.__time_log = log
    
    
    # SETTER 
    def set_bot(self, name:str) -> None:
        """Set Bot Name
        Args:
            name (str)
        """
        self.__BOT_NAME = name 
    
    def set_born(self, date:datetime) -> None:
        self.__BORN = date
        
    def set_user(self, user:str) -> None:
        self.__USER = user
    
    
    # GETTER
    def get_bot_name(self) -> str:
        """Get Bot Name
        Returns:
            str: Bot Name
        """
        return self.__BOT_NAME
    
    
    def get_bot_birth_date(self) -> datetime:
        """_summary_

        Returns:
            datetime: Bot birth date
        """
        return self.__BORN
    
    
    def get_user(self):
        return self.__USER
    
    def get_BOT(self):
        return self.__BOT
    
    def get_PATH(self):
        return self.__PATH
    
    def get_SCHEDULE(self):
        return self.__SCHEDULE
    
    
    # SETTING
    def change_bot_name(self, name:str) -> None:
        with open(self.__BOT, 'r') as bot:
            data = json.load(bot)

        data['_Bot__BOT_NAME'] = name
        
        with open(self.__BOT, 'w') as bot:
            json.dump(data, bot)
        
        self.set_bot(name)
    
    # Bot init
    def bot_init(self, path:str):
        with open(path, 'r') as bot:
            data = json.load(bot)
            self.set_user(data['_Bot__USER'])
            self.set_bot(data['_Bot__BOT_NAME'])
    
    def default_msg(self):
        print(f"Hello {self.get_user()}, {self.get_bot_name()} here. How can I help ?")