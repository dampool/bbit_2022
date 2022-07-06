#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security

class securityInterface():
    def __init__(self, name: str) -> None:
        pass
    
    def getName(self) -> str:
        return "Implement Me!"
    
class security():
    def __init__(self,name:str):
        self.name = name
        
    def getName(self):
        return self.name
