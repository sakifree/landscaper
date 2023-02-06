## Game State

game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0},
    {"name": "rusty scissors", "profit": 5, "cost": 5},
    {"name": "old-timey push mower", "profit": 50, "cost": 25},
    {"name": "fancy battery-powered mower", "profit": 100, "cost": 250},
    {"name": "hire team of starving students", "profit": 250, "cost": 500}
]

while(True):
    user_choice = input("[1] Mow Lawn [2] Check Stats [Q] Quit ")
    
    if(user_choice == 1):
        pass
    elif(user_choice == 2):
        pass
    elif(user_choice == "Q"):
        break
    else:
        print("Invalid input. Please select 1, 2, or Q.")