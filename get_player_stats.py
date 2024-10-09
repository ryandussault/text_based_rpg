

def get_player_stats():
    sword = {"class": "weapon", "weapon_name": "Sword", "Damage": 5, "adress": "2"}
    stats_dict = {}
    inventory = {"Slot 1": "empty", "Slot 2":"empty", "Slot 3":"empty", "Slot 4":"empty", "Slot 5":"empty", "Slot 6":"empty", "Slot 7":"empty", "Slot 8":"empty", "Slot 9":"empty", "Slot 10":"empty", "Gold": 30}

    #gets character name
    name = input("What is your name traveler? \n")
    print("Well hello there young "+name)
    stats_dict["Name"] = name
    stats_dict["health"] = 15
    stats_dict["health_max"] = 15
    
    #gets class, weapon, or spell
    while True:
        player_class = input("If you don't mind my asking, how do you fight? \n(1 for Melee, 2 for Wizard)\n")
        if player_class == "1":
            stats_dict["Class"] = "Melee"
            print("Every good Melee Fighter needs a sword. \nYou can have this one.")

            inventory["Slot 1"] = sword
            break

        elif player_class == "2":
            stats_dict["Class"] = "Wizard"
            print("It's good to have a new wizard in town, take my spell of \"Ouch!\"")
            ouch = {"class": "weapon", "weapon_name": "Ouch!", "Damage": 5, "adress": "3"}
            inventory["Slot 1"] = ouch
            break
        else:
            print("Im not sure I caught that.")
    
    return stats_dict, inventory