from assistant import Assistant
import random

class System(Assistant):
    
    def __init__(self):
        super().__init__()
        self.__func = {1:self.change_bot_name,
                       2:self.create_schedule,
                       3:self.show_schedule,
                       4:self.throw_jokes,
                       5:self.send_email,
                       6:self.shut_down}
        
    def run(self):
        
        while True:
            print("")
            self.default_msg()
            print("""
    1. Change bot name
    2. Create schedule
    3. Show schedule
    4. Jokes
    5. Send Email
    6. Shut Down
                """)
            
            try:
                input_user = int(input(">> "))
                self.__func[input_user]()
            except ValueError as e:
                print(f"Oops.. {e.__class__.__name__}. Please select using number !")
    
    
    def change_bot_name(self) -> None:
        
        name = input('New bot name: ')    
        return super().change_bot_name(name=name)
    
    
    def create_schedule(self):
        print("Create agenda")
        date = input("Date (dd/mm/yyyy): ")
        agenda = input("Agenda: ")
        return super().create_schedule(date, agenda)
    
    def show_schedule(self):
        print("List Schedule")
        print("=============")
        try:
            for i, agenda in enumerate(super().show_schedule().split('\n')):
                print(f"{i}. {agenda}")
        except:
            print("No Schedule !")
    
    def throw_jokes(self):
        while True:
            jokes = super().throw_jokes()
            try:
                print(random.choice(jokes.split("\n")))
                print("Haha, funny right. You want more? (yes/no)")
                input_user = input(">> ")
                if input_user.lower() != "yes":
                    break
            except:
                print("sorry I'm not having humor now")
                break
            
            