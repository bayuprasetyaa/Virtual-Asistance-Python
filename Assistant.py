# Case Study: Virtual Assistant using Python (Assistant.py)

# CLUE: import necessary libraries here

class Bot:

    def __init__(self, name):
        
        self.__name = name
    
    def set_bot(self, name:str) -> None:
        """Set Bot Name
        Args:
            name (str)
        """
        pass 
    
    def get_bot(self) -> str:
        """Get Bot Name
        Returns:
            str
        """
        pass

class Assistance(Bot):
    
    def __init__(self):
        super().__init__()
    
    def create_schedule(self):
        pass
    
    def show_schedule(self):
        pass
    
    def throw_jokes(self):
        pass
    
    def send_email(self):
        pass
    