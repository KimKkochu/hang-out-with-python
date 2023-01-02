class User:
    def __init__(self, Name:str) -> None:
        # 0 equal 'empty'
        self.default_setting = {
            'Name': Name,
            'inventory' : [[{0:0} for i in range(3)] for i in range(3)]
        }
        self.r_hand_set(0, 0)
        
    def r_hand_set(self, row:int, column:int):
        self.default_setting['R_hand'] = self.default_setting['inventory'][row][column]
    
    def get_item(self, item):
        pass


class Lighter(User):
    def __init__(self, Name: str) -> None:
        super().__init__(Name)
        

Person = User('Elon')

print(Person.default_setting)
