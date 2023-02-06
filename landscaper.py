## Game State

game = {"tool": 0, "money": 0}

tools = [
    {"name": "Teeth", "profit": 1, "cost": 0},
    {"name": "Rusty Scissors", "profit": 5, "cost": 5},
    {"name": "an Old-Timey Push Mower", "profit": 50, "cost": 25},
    {"name": "a Fancy Battery-Powered Mower", "profit": 100, "cost": 250},
    {"name": "a Team of Starving Students", "profit": 250, "cost": 500}
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
    if(game["tool"] == 4 and game["money"] >= 1000):
        print(f"You Win! You ended with {game['money']} dollars!git ")
        return True
    return False  
    
while(True):
    user_choice = input("[1] Mow Lawn [2] Check Stats [3] Upgrade Tool [4] Quit ")
    user_choice = int(user_choice)
    if(user_choice == 1):
        mow_lawn()
    elif(user_choice == 2):
        check_stats()
    elif(user_choice == 3):
        upgrade()
    elif(user_choice == 4):
        print("You quit the game")
        break
    else:
        print("Invalid input. Please select 1, 2, or 4.")
        
    if (win_check()):
        break