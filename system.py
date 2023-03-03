from assistant import Assistant

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
            
            