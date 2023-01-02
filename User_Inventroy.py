User_Name = set()

class User:
    def __init__(self, Name:str) -> None:
        # 0 equal 'empty'
        self.default_setting = {
            'Name': Name,
            'inventory' : [[{0:0} for i in range(3)] for i in range(3)],
            'Stack_point': [0, 0] # [row, column]
        }
        self.r_hand_set(0, 0)
        User_Name.add(Name)
        
    def r_hand_set(self, row:int, column:int):
        self.default_setting['R_hand'] = self.default_setting['inventory'][row][column]

class Lighter(User):
    def __init__(self, Name):
        pass

        

Person = User(Name='Elon')
