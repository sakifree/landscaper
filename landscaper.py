## Game State

game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0},
    {"name": "rusty scissors", "profit": 5, "cost": 5},
    {"name": "old-timey push mower", "profit": 50, "cost": 25},
    {"name": "fancy battery-powered mower", "profit": 100, "cost": 250},
    {"name": "hire team of starving students", "profit": 250, "cost": 500}
]

## Game Option Functions

def mow_lawn():
    tool = tools[game["tool"]]
    print(f"You mowed a lawn with your {tool['name']} and make {tool['profit']}")
    game["money"] += tool["profit"]

def check_stats():
    tool = tools[game["tool"]]
    print(f"You currently have {game['money']} and are using {tool['name']}")
    
def upgrade():
    next_tool = tools[game["tool"]+1]
    if (next_tool == None):
        print("There is no more tools")
        return 0
    if (game["money"] < next_tool["cost"]):
        print("Not enough to buy tool")
        return 0
    game["money"] -= next_tool["cost"]
    game["tool"] += 1
    
def win_check():
    if(game["tool"] == 4 and game["money"] == 1000):
        print("You Win")
        return True
    return False  
    
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