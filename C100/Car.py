

class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        
    def start(self):
        print("STARTED "+ self.model)
        
    def stop(self):
        print("STOPPED")
    
    def accelerate(self):
        print("ACCELERATING")
    
    def change_gear(self,gear_type):
        print("Gear Change")
        
        
car1 = Car("A6","Red","Audi",180)

car1.start()