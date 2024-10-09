from get_player_stats import get_player_stats
from time import sleep
from items import items_weapons_armor
from random import choice



sword, ouch, health_potion, rusty_sword, shiny_sword, sharp_sword, stabbies_sword, fire_spell, acid_spell, wanda_wizard_spell, leather_armor, chain_mail_armor, steel_armor, amos_armor, candy_cane_sword, poor_witches_spell, claw, comically_large_spoon, magic_revolver, lazy_tail, the_law, bomb, beard_missles, dragon_sword = items_weapons_armor()

did_easy_quest = False
did_hard_quest = False
true_loop_breaker = False

print(" _____ _            ____        _ _           _          __ ")
print("|_   _| |__   ___  | __ )  __ _| | | __ _  __| |   ___  / _|")
print("  | | | '_ \ / _ \ |  _ \ / _` | | |/ _` |/ _` |  / _ \| |")
print("  | | | | | |  __/ | |_) | (_| | | | (_| | (_| | | (_) |  _|")
print("  |_| |_| |_|\___| |____/ \__,_|_|_|\__,_|\__,_|  \___/|_| ")
print("")
print(" ____")
print("/ ___|  ___  _ __ ___   ___")
print("\___ \ / _ \| '_ ` _ \ / _ \\")
print(" ___) | (_) | | | | | |  __/")
print("|____/ \___/|_| |_| |_|\___|")
print("\n")
sleep(1.5)
print(" ____            _       __        ___             _____ _       _     _       ")
print("|  _ \ _   _  __| | ___  \ \      / / |__   ___   |  ___(_) __ _| |__ | |_ ___")
print("| | | | | | |/ _` |/ _ \  \ \ /\ / /| '_ \ / _ \  | |_  | |/ _` | '_ \| __/ __|")
print("| |_| | |_| | (_| |  __/   \ V  V / | | | | (_) | |  _| | | (_| | | | | |_\__ \\")
print("|____/ \__,_|\__,_|\___|    \_/\_/  |_| |_|\___/  |_|   |_|\__, |_| |_|\__|___/")
print("                                                           |___/")
print("")
print(" _____ _     _")
print("|_   _| |__ (_)_ __   __ _ ___")
print("  | | | '_ \| | '_ \ / _` / __|")
print("  | | | | | | | | | | (_| \__ \\")
print("  |_| |_| |_|_|_| |_|\__, |___/")
print("                     |___/")
sleep(1.1)

player_stats, inventory = get_player_stats()


def main():
    # main, does nothing
    start()



    
def start():
    # start, also does basically nothing
    print(f'You wake up from the mysterious dream in the middle of the street, suprised to feel the {inventory["Slot 1"]["weapon_name"]} the voice gave you in it\'s holster')
    town_square()





def inn():
    # function for the inn, used for out of fight healing and looking at inventory
    sleep(1)
    print("You enter the Inn, It is well lit and looks warm and cozy.")

    while True:
        # loop for determining player action
        action = input("The inkeeper gives you a warm smile and asks: \nWould you like: \n1. A room (3 gold, Restores you to full Health) \n2. A Meal (2 Gold, Restores 10 Health) \n3. Look at inventory \n4. Leave\n")
        sleep(1)
        if action == "1":
            if inventory["Gold"] >= 3:
                # returns player to max health
                inventory["Gold"] = inventory["Gold"] - 3
                player_stats["health"] = player_stats["health_max"]
                print("You sleep off your pain in a cozy bed.")
                sleep(0.75)
                print(f"You now have {player_stats['health']} health.")
                sleep(1.2)
            # shows message if player can't afford item
            elif inventory["Gold"] < 3:
                print("You do not have enough gold for this item.")

        elif action == "2":
                # gives the player 10 health, then checks if it is over the max health, and if so, sets the player health to the max health
                if inventory["Gold"] >= 2:
                    inventory["Gold"] = inventory["Gold"] - 2
                    player_stats["health"] = player_stats["health"] + 10
                    if player_stats["health"] > player_stats["health_max"]:
                        player_stats["health"] = player_stats["health_max"]
                
                    print("The inkeeper, upon payment, cooks you a delicious meal.")
                    sleep(0.5)
                    # prints players health
                    print(f"You now have {player_stats['health']} health.")
                
                elif inventory["Gold"] < 2:
                    # shows message if player can't afford item
                    print("You do not have enough gold for this item.")
        
        elif action == "3":
            # prints out player inventory
            for key in inventory:
                sleep(0.25)
                try:
                    # checks if the slot is empty, and if not, runs theough if statements until the item class is reached, only three possible classes
                    if inventory[key] == "empty":
                        print(f"{key}: {inventory[key]}")
                    else:
                        if inventory[key]["class"] == "weapon":
                            print(f"{key}: {inventory[key]['weapon_name']}")

                        elif inventory[key]["class"] == "potion":
                            print(f"{key}: {inventory[key]['potion_name']}")

                        elif inventory[key]["class"] == "armor":
                            print(f"{key}: {inventory[key]['armor_name']}")
                except TypeError:
                    # when the "gold" key is reached a type error is thtrown which tells the program to print out the gold amount
                    print(f"Gold: {inventory['Gold']}") 
            sleep(0.25)
            # prints health and max health    
            print(f"Health: {player_stats['health']}")
            sleep(0.25)
            print(f"Max health: {player_stats['health_max']}")             




        elif action == "4":
            print("You decide to leave the inn.")
            sleep(0.5)
            town_square()
            break


def shopping_district():
    # hub for shops
    sleep(0.75)
    
    while True:
        # loop for player input
        shops = input("You round the corner into the shopping district. you can go to: \n1. Tavern \n2. Potion Shop \n3. Armor Shop \n4. Melee Shop \n5. Spell Shop \n6. Leave\n")
        if shops == "1":
            tavern()
            break
        elif shops == "2":
            potion_shop()
            break
        elif shops == "3":
            armor_shop()
            break
        elif shops == "4":
            weapons_shop()
            break
        elif shops == "5":
            spell_shop()
            break
        elif shops == "6":
            town_square()
            break
        else:
            print("input not recognized, please type in the number associated with the action\n")

def spell_shop():
    # func for the spell shop
    # discriminatory
    sleep(0.5)
    print("The sign above the spell shop reads 'Wanda Wizards Workshop of Wacky Wild Enchantments'.")
    sleep(1)
    print("You walk into the small shop.") 
    if player_stats['Class'] == "Wizard":
        # if statement to determine class
        print("The shopkeeper, who you assume to be Wanda Wizard greets you.")
        sleep(0.75)
        while True:
            # loop for determining item choice
            item = input(f"Wanda points to the sign on the wall. It says: \nThe spells currently available are: \n1. {fire_spell['weapon_name']}, (25 Gold, 7 Damage) \n2. {acid_spell['weapon_name']}, (40 gold, 10 damage) \n3. {wanda_wizard_spell['weapon_name']}, (75 gold, 12 damage) \n4. Leave\n")

            #spell 1
            if item == "1" and inventory["Gold"] >= 25:
                buy_stuff(25, fire_spell["weapon_name"], fire_spell, armor=False)
            
            elif item == "1" and inventory["Gold"] < 25:
                sleep(0.5)
                print("You do not have enough gold for this spell.")
                sleep(1)
            
            #spell 2
            elif item == "2" and inventory["Gold"] >= 40:
                buy_stuff(40, acid_spell["weapon_name"], acid_spell, armor=False)
            
            elif item == "2" and inventory["Gold"] < 40:
                sleep(0.5)
                print("You do not have enough gold for this spell.")
                sleep(1)

            #spell 3
            elif item == "3" and inventory["Gold"] >= 75:
                buy_stuff(75, wanda_wizard_spell["weapon_name"], wanda_wizard_spell, armor=False)
            
            elif item == "3" and inventory["Gold"] < 75:
                sleep(0.5)
                print("You do not have enough gold for this spell.")
                sleep(1)

            #leave
            elif item == "4":
                sleep(0.5)
                print("You decide to leave the shop.")
                sleep(0.25)
                shopping_district()
                break

            else:
                print("Input not recognized.")

    else:
        sleep(0.5)
        # discrimination
        print("Wanda wizard kicks you out because you are lowly melee scum.")
        sleep(0.5)
        shopping_district()


def woods():
    # place that gives quests

    # bools to prevent players from doing quests twice
    global did_easy_quest, did_hard_quest
    print("You see a dirt path leading to a thick forest. After walking for what seemed like hours, you come across a sign.")
    sleep(1)
    print("There is an arrow pointing to the left that says \"Super Easy Fun Starting Adventure\" and one pointing to the right that says \"Super Hard Last Adventure\".")
    sleep(1)
    while True:
        # loop to determine player choice
        choice = input("1. Left \n2. Right \n3. Leave\n")
        if choice == "1":
            if did_easy_quest == False:
                did_easy_quest = True
                # starts the easy adventure
                easy_adventure()
                break
            else:
                print("Quest completed. You can't do it again.")

        elif choice == "2":
            if did_hard_quest == False:
                did_hard_quest = True
                # starts the hard adventure 
                hard_adventure()
                break
            else:
                print("Quest completed. You cab't do it again.")

        elif choice == "3":
            # leaves the woods, back to the town square
            town_square()
            break
        else:
            print("Input not recognized.")

def easy_adventure():
    # rude to player
    print("Because you are a little wimp, you decide to go down the path on the left. After just a few minutes of walking, the dark forest turns into a candyland of dreams.")
    sleep(2)
    print("As you walk, you hear the laughs of two children. As you near them, you see the largest, most exorbitant candy house of all time.")
    sleep(2)
    print("The two children are munching away on a beautiful gingerbread facade. You wonder to yourself whose house this is.")
    sleep(2)
    print("Your answer comes quickly, as a witch runs out of the forest, shaking her fist like an old hag at the ruffians the decided to eat her house.")
    sleep(2)
    

    while True:
        # determines who the player wants to help, starts the function related to player choice, killing children is line 1, witch is line 2
        choice = input("You can: \n1. Help the witch fight off the ruffians \n2. Help the ruffians fight the witch\n")
        if choice == "1":
            print("Because you are a good samaritan, you decide to help the witch fight off the ruffians.")
            sleep(1)
            # fight against children
            enemy(weapon=candy_cane_sword, health=6, gold=2, name="Bastard Children", voice_line=None)
            print("The nice witch thanks you for vanquishing the children back to their parents. You decide to keep going along the path")
            sleep(1)
            # line 1.1 
            easy_adventure_just_killed_children()
            break
        elif choice == "2":
            print("Because you are a total prick, you decide to help the children who are eating the poor witches house.")
            sleep(1)
            # fight against witch
            enemy(weapon=poor_witches_spell, health=9, gold=9, name="The Poor Witch With Children Eating Her House", voice_line="Why would you help those horrible children! They are ruining my house!")
            sleep(1)
            print("The witch that just wanted her house to not be eaten looks at you as she slowly bleeds out from her wounds. The children don't even blink.")
            # line 2.1
            easy_adventure_just_killed_poor_nice_witch()
            break


# line 1.1
def easy_adventure_just_killed_children():
    # interaction with npc
    print("After helping that poor witch, a large orc pops out of the woods, carrying a comically large spoon.")
    sleep(3)
    print("You ask him where he is going.")
    sleep(2)
    print("He replies that he is going over to the witches house and asks you if you had seen her.")
    sleep(3)
    print("You reply, telling him about the ordeal with those children.")
    sleep(3)
    print("He explains that he is a friend of the witch and that she is always lamenting about the horrible children who keep eating her house.")
    sleep(3)
    print("To thank you, he gives you a heavy sack that he found on the path.")
    sleep(3)
    print("After the nice orc goes on his way, you decide to see what is in the bag.")
    sleep(3)
    print("To you surprise, the bag is filled with the shiniest gold coins that you have ever layed you eyes on.")
    sleep(3.5)
    inventory["Gold"] = inventory["Gold"] + 35
    print(f"There are 25 gold pieces in the sack. You now have {inventory['Gold']} gold.")
    # line 1.2
    easy_adventure_just_killed_children_part_2()


# line 1.2
def easy_adventure_just_killed_children_part_2():
    # enemy encounter
    sleep(3)
    print("You ponder the odd meeting with the orc, not thinking much of it.")
    sleep(3)
    print("You walk another mile, amazed that all of the plants and animals are made out of candy.")
    sleep(3)
    print("For some reason, the hairs on the back of your neck stand up.")
    sleep(4)
    print("You hear rustling in the cotton candy bushes.")
    sleep(2)
    print("A talking, non candy wolf pops out of the bushes! He yells something about licking all of the candy creatures so that they stick together.")
    sleep(4)
    print("It is your duty to the candy forest to stop him!")
    # function call to start enemy fight
    enemy(weapon=claw, health=12, gold = 17, name="Big Bad Wolf", voice_line="I'm the Big Bad Wolf!. I'm gonna rip your flesh from your bones!")
    sleep(3)
    print("After a hard battle against the wolf, you wonder if you shold visit the inn for the night an heal up or maybe get some health potions.")
    sleep(1)
    # sends player back to town square
    town_square()
    

# line 2.1
def easy_adventure_just_killed_poor_nice_witch():
    # enemy encounter
    sleep(3)
    print("After brutally murdering the poor witch, a large orc pops out of the woods, carrying a comically large spoon.")
    sleep(3)
    print("He asks you where you are going, and you tell him that you just came from the candy house and are exploring deeper into the candy woods.")
    sleep(3)
    print("The orc questions you about the house, asking if you saw the witch.")
    sleep(3)
    print("You fail the charisma roll and tell the orc that you murdered the poor witch in cold blood to help some children.")
    sleep(3)
    print("This enrages the orc. You wonder if they were friends.")
    sleep(3)
    # function to start fight
    enemy(weapon=comically_large_spoon, health=14, gold = 35, name="Orceus, Defender of Witches", voice_line="You dare kill that nice witch, tiny human! I will drink your blood!")
    sleep(2)
    print("Somehow, you managed to defeat Orceus, but you did not escape unscathed.")
    sleep(3)
    print("In light of your horrid misdeeds, you decide to go deeper into the candy forest.")
    sleep(3)
    # func to start line 2.2
    easy_adventure_just_killed_poor_nice_witch_part_2()

# func for line 2.2
def easy_adventure_just_killed_poor_nice_witch_part_2():
    # npc encounter
    print("You walk for over an hour, before anything happens.")
    sleep(3)
    print("You hear a cotton candy bush rustle behind you.")
    sleep(3)
    print("You whip your head around and see a talking wolf!")
    sleep(3)
    print("The wolf eyes you up and down before speaking. He tells you about what he witnessed you do earleir.")
    sleep(3)
    print("He tells you how nice it is to find someone else who takes a sick pleasure in killing nice, upstanding witches and orcs.")
    sleep(3)
    print("He gives you a pouch packed to the brim with gold coins as a favor for getting rid of the witch and her pesky orc.")
    sleep(3)
    # adds gold to inventory
    inventory["Gold"] = inventory["Gold"] + 25
    print(f"The pouch contains 20 gold. You now have {inventory['Gold']} gold, you horrible, scum of the earth.")
    sleep(3)
    print("You leave the forest, your name tarnished.")
    town_square()

# hard adventure
def hard_adventure():
    # fun logic cause i nested true loops
    global true_loop_breaker
    print("You, being a very brave adventurer, decide to take the path on the right.")
    sleep(3)
    print("You walk for 30 minutes of uniterupted peace, until suddenly, a bandit pops out of the foliage!")
    sleep(3)
    print("You watch in terror as he pulls a magic smith & wesson that shoots magic bullets!")
    sleep(3)
    while True:
        # choice
        choice = input("You can: \n1. Defend yourself from Bandy McBandit Face \n2. Try to talk him down\n")
        sleep(2)


        if choice == "1":
            # enemy encounter
            enemy(weapon=magic_revolver, health=15, gold=17, name="Bandy McBandit Face", voice_line="I am Bandy McBandit Face and I want your gold!")
            # starts next part
            hard_adventure_line_1()
            break


        elif choice == "2":
            print("You decide to try and talk the crazed bandit out of robbing you!")
            sleep(3)
            print("He tells you there won't be any trouble if you just empty your pockets")
            sleep(3)
            print("Because you lost your chance of first attack, you can either empty your pockets or try one more time to talk him out of his crime.")
            sleep(2)

            # nested true loop
            while True:
                # more choice
                choice_1 = input("1. Give him 25 gold (or as much as is in your pockets) \n2. Keep talking to avoid giving him money\n")
                
                # takes gold and starts line 2 of the adventure
                if choice_1 == "1":
                    inventory["Gold"] = inventory["Gold"] - 25
                    if inventory["Gold"] < 1:
                        inventory["Gold"] = 0
                    print(f"You now have {inventory['Gold']} gold remaining.")
                    hard_adventure_line_2()
                    true_loop_breaker = True
                    break
                
                elif choice_1 == "2":
                    # wrong choice, bandit kills player, the end
                    hard_adventure_die_to_bandit()
                    true_loop_breaker = True
                    break

                else:
                    print("Input not recognized.")
                    sleep(1)
        else:
            print("Input not recognized")

        if true_loop_breaker == True:
            break

def hard_adventure_line_1():
    # heals player, npc encounter, choice for line 1.1 or 1.2
    sleep(2)
    print("After fighting the bandit, you decide to continue along the trail, wary of every rustle.")
    sleep(3)
    print("You can't even explore the woods without someone attacking you. Its almost like you're the main character in this towns story or something.")
    sleep(3)
    print("As you walk, you notice that something is following you. You decide to keep your gaze straight ahead, hoping to avoid another fight.")
    sleep(3)
    print("Suddenly, a voice very low to the ground calls out, \"I know you know I'm here.\"")
    sleep(3)
    print("You turn around, and to your surprise, the voice came from a cat!")
    sleep(3)
    print("The cat tells you that you look, like, totally cool after you fought that bandit, and decides to gift you some catnip.")
    sleep(3)
    print("You graciously accept the offering from the cat and get full health!")
    sleep(2)
    player_stats["health"] = player_stats["health_max"]
    print(f"You now have {player_stats['health']} health remaining.")
    sleep(2)

    print("The cat tells you about 2 great dragons, siblings, that lay ahead on the path.")
    sleep(3)
    print("The cat gives you a stipulation though, If you attack one dragon, the other will fly away.")
    sleep(3)
    print("You know you must kill one of the dragons, but which one?")
    sleep(3)
    print("You can go after DJ Fax Machine (he's a failure, his parents hate him), or Mr. Lawyer.")
    sleep(2)

    while True:
        # player choice
        choice = input("1. DJ Fax Machine (super lazy) \n2. Mr. Lawyer (probably rich)\n")

        if choice == "1":
            sleep(2)
            # boss encounter 1.1
            hard_adventure_DJ_fax_machine()
            break
        
        elif choice == "2":
            sleep(2)
            # boss encounter 1.2
            hard_adventure_Mr_lawyer()
            break

        else:
            print("Input not recognized")


def hard_adventure_DJ_fax_machine():
    # boss encounter 1.1
    print("You decide to challenge DJ Fax Machine!")
    sleep(3)
    print("You thank the cat and continue on the path.")
    sleep(2)
    print("After a short walk you come across DJ Fax Machine.")
    sleep(2)
    # func for fight
    enemy(weapon=lazy_tail, health=20, gold=4, name="DJ Fax Machine", voice_line="Once he see's you, he says , \"Hey, get out of my studio. I'm gonna get my brother to sue you!\"")
    sleep(2)
    print("After defeating the smelliest dragon in the land, you decide to go back to town.")
    sleep(1)
    # returns player back to the town square
    town_square()


def hard_adventure_Mr_lawyer():
    # boss encounter 1.2
    print("You, being ever so brave, decide to banish Mr. Lawyer.")
    sleep(3)
    print("You thank the talking cat and meander on down to Mr. Lawyer's Mr. Mansion.")
    sleep(2)
    print("After walking up an exorbitantly long drive way, you see the formidable dragons house.")
    sleep(2)
    enemy(weapon=the_law, health=25, gold=65, name="Mr. Lawyer", voice_line="I'm Mr. Lawyer and you have the right to remain silent. Oink, Oink!")
    # func for fight, see also: lawyer hate
    sleep(2)
    print("After your glorious defeat of Mr. Lawyer, you decide to head back to the town.")
    sleep(1)
    # return player to town square
    town_square()

def hard_adventure_die_to_bandit():
    # player death from wrong choice
    sleep(2)
    print("You decide to Try one more time to convince the crazed bandit to put down the gun.")
    sleep(3)
    print("He gets even more jumpy and when you reach out to stop him, he shoots you.")
    sleep(3)
    print("You bleed out on the ground because of his magic bullets.")
    sleep(2)
    exit(code="Exit Code 14: nerd you died trying to help someone")

def hard_adventure_line_2():
    # line 2 of hard adventure, more insulting player, player choice
    sleep(2)
    print("Because you're a little nerd, you give the bandit your money.")
    sleep(2)
    print("You decided to keep walking in a poor attempt to hide your shame.")
    sleep(2)
    print("After a mile or two, you hear something behind you, but decide to keep looking straight ahead to prevent another embarassing situation like the one that just took place.")
    sleep(4)
    print("After another half mile, a voice near the gound says, \"I know you know that i'm behind you.\"")
    sleep(3)
    print("You look back and see a talking cat!")
    sleep(2)
    print("The cat shames you about what happened with the bandit, cause he is a jerk.")
    sleep(3)
    print("After another humiliating interaction, cause you won't stand up for yourself, you come across a split in the path.")

    while True:
        # player choice for split in the path
        choice = input("1. Left \n2. Right\n")

        if choice == "1":
            # boss fight 2.1.1
            hard_adventure_2_1_1()
            break
        elif choice == "2":
            # boss fight 2.1.2
            hard_adventure_2_1_2()
            break
        else:
            print("Input not recognized.")


def hard_adventure_2_1_1():
    # boss fight 2.1.1
    sleep(2)
    print("You decide to take the path on the left. As you walk the forest gets dark and scary.")
    sleep(3)
    print("You hear explosions in the distance and they get louder as you walk.")
    sleep(3)
    print("You see a man atop a rock blowing up the country side.")
    sleep(2)
    print("You think to yourself, \"Could this be Tim the Enchanter.\"")
    sleep(2)
    print("The man disappears in a huge explosion, and then suddenly reappears next to you.")
    sleep(3)
    print("\"I am Tim and I challange you\" says tim.")
    sleep(2)
    # func for starting fight, see also: monty python reference. credits: dad
    enemy(weapon=bomb, health=30, gold=42, name="Tim the  Enchanter", voice_line="I'm Tim the Enchanter and I'm gonna blow you up.")
    sleep(2)
    print("Wow!, You won, didn't expect that, You go back to town to get some rest or something.")
    # returns player to town square
    town_square()


def hard_adventure_2_1_2():
    # if you haven't figured this out by now you should probably take acourse or something, same stuff as func right before it
    sleep(2)
    print("You decide to take the path on the right. As you walk the forest gets wierdly grey.")
    sleep(3)
    print("You hear beard hairs growing in the distance, getting louder as you near their source.")
    sleep(3)
    print("You see a man atop a rock grooming the most luscious gray beard you have ever seen.")
    sleep(3)
    print("You think to yourself, \"Could this be Gandalf the Beardy.\"")
    sleep(2)
    print("The man disappears in a kerfuffle of beard hair, and then suddenly reappears next to you.")
    sleep(3)
    print("\"I am Gandalf the Beardy and I challange you\" says Gandalf.")
    sleep(2)
    enemy(weapon=beard_missles, health=25, gold=50, name="Gandalf the Beardy", voice_line="I'm gonna beard all over you!")
    sleep(2)
    print("Wow!, You won, did you have fun being bearded? You go back to town to get some rest or something, maybe clean out those hairs.")
    town_square()


def mysterios_tavern_man_quest():
    # start of tavern quest, determines of the player actually wants to do it, if not player is sent back out to the shopping district
    print("You decide to sit across from the hooded figure.")
    sleep(2)
    print("\"Are you the adventurer I've heard so much about?\" he asks.")
    sleep(2)
    print("You reply, confirming his suspicions.")
    sleep(1.5)
    print("He tells you about a great wepon that only the worthy can wield. He tells you it is up in the mountains of I'm Not Making Anymore Names.")
    sleep(3)
    while True:
        choice = input("You can: \n1. Accept his quest \n2. Deny his offer and leave\n")

        if choice == "1":
            tavern_quest_1()
            break
        elif choice == "2":
            shopping_district()
            break
        else:
            print("Input not recognized")


def tavern_quest_1():
    # part 1 of the tavern quest
    print("You decide to accept the quest from the shady dude in a bar, proving that you can make smart decisions.")
    sleep(3)
    print("The mountains are just south of the town. Their peaks are visible from the town square.")
    sleep(3)
    while True:
        # determine player choice, option one completes the quest, but takes 5 irl minutes cause why not
        choice = input("You start your journey south. The walk should take 5 minutes. \n1. Walk (Patience is rewarded) \n2. Embark on this quest later\n")
        sleep(1)
        if choice == "1":
            # waits for 5 minutes
            sleep(300)
            tavern_quest_2()
            break

        elif choice == 2:
            # return player to town square
            town_square()
            break

        else:
            print("Input not recognized.")

def tavern_quest_2():
    print("Whew. That was a long walk. You can see the cave in which this fabled weapon resides.")
    sleep(3)
    print("It looks old and decrepted. You notice that is is unguarded, probably because it is so old.")
    sleep(3)
    print("You walk up to the famed weapon, roll a 20 perception check, and suddenly, it's name comes to you in a vision!")
    sleep(3)
    # uses cowsay to make an ascii dragon say "Dragon Sword of Death", used to, exe wouldn't work with this in
    print("Dragon Sword of Death")
    # puts super cool dragon sword in players inventory
    buy_stuff(0, "Dragon Sword of Death", dragon_sword, armor=False)
    sleep(2)
    print("You sleep walk back to town and it only takes 2 seconds.")
    sleep(2)
    town_square()



def tavern():
    # indiscriminatory
    sleep(1)
    print("You swing open the door to \"Boggle-Schnoggle Tavern\", underestimating its creakiness.")
    sleep(0.5)
    print("Every patron turns to stare at you. You notice a mysterious man in the corner sitting by himself.")
    sleep(0.5)
    while True:
        # loop for determining user action, tavern also gives a quest
        action = input("Do you:\n1. Get a Drink \n2. Talk to the bartender \n3. Talk to the mysterious man \n4. Leave \n")
        if action == "1":
            print("You get a beer from the bartender, but it tastes like piss so you dump it out")
            sleep(0.75)
        elif action == "2":
            print("You ask the bartender about the name of the bar. \nHe explains that it is a family name and then refuses to elaborate.")
            sleep(0.75)
        elif action == "3":
            # hidden quest
            mysterios_tavern_man_quest()
            sleep(0.75)
            break
        elif action == "4":
            print("You leave the tavern and enter the shopping district.")
            sleep(0.75)
            shopping_district()
            break
        else:
            print("input not recognized, please type in the number associated with the action\n")


def potion_shop():
    # indiscriminatory
    print("You walk into the potion shop. \nThe shelves of potions look dusty and old, just like the shop keeper")
    sleep(2)
    print("She looks at you for a second to long before speaking: \"I offer some of the finest potions in town, to those who are willing to buy them\".")
    sleep(1.75)

    while True:
        # loop determining if the user wants a health potion or go leave
        potions = input("You look at the yellowing sign hanging from the shopkeepers counter. \nThere are 3 potions listed there, but next to the attack and defense potions, there is an out of stock marking. \nyou can:\n1. Health potion: restores 10 health to user, 5 gold \n2. Leave\n")
        if potions == "1" and inventory["Gold"]>=5:
            buy_stuff(5, health_potion["potion_name"], health_potion, armor=False)

        elif potions == "1" and inventory["Gold"] < 5:
            sleep(0.5)
            print("You do not have enough Gold for this potion.")
            sleep(3)
            print("The shop keeper has kicked you out for loitering.")
            shopping_district()
            break


        elif potions == "2":
            shopping_district()
            break
        else:
            print("Input not recognized")


def armor_shop():
    # indiscriminatory
    sleep(0.75)
    print("The shops sign says 'Amos's Ample Armor Emporium'.")
    sleep(0.5)
    print("You walk through the door.")
    while True:
        # loop for determing what item the player wants, checking if the have enough gold before adding to inventory
        sleep(0.5)
        armor = input("The shops sign displays 3 items (and the disclaimer: Buying a new set of srmor destroys the current set.): \n1. Leather Armor (25 Gold, 1 Defence) \n2. Knightly Chain Mail Armor (40 gold, 2 Defense) \n3. Knightly Steel Plate Armor (60 Gold, 3 Defense) \n4. Amos's Ample Armor (75 Gold, 4 Defence) \n5. Leave\n")

        #armor 1
        if armor == "1" and inventory["Gold"] >= 25:
            buy_stuff(25, leather_armor["armor_name"], leather_armor, armor=True)

        elif armor == "1" and inventory["Gold"] < 25:
                sleep(0.5)
                print("You do not have enough Gold for this item.")
                sleep(1)
        
        #armor 2
        elif armor == "2" and inventory["Gold"] >= 40:
            buy_stuff(40, chain_mail_armor["armor_name"], chain_mail_armor, armor=True)

        elif armor == "2" and inventory["Gold"] < 40:
                sleep(0.5)
                print("You do not have enough Gold for this item.")
                sleep(1)
        
        #armor 3
        elif armor == "3" and inventory["Gold"] >= 60:
            buy_stuff(60, steel_armor["armor_name"], steel_armor, armor=True)

        elif armor == "3" and inventory["Gold"] < 60:
                sleep(0.5)
                print("You do not have enough Gold for this item.")
                sleep(1)

        #armor 4
        elif armor == "4" and inventory["Gold"] >= 75:
            buy_stuff(75, amos_armor["armor_name"], amos_armor, armor=True)

        elif armor == "4" and inventory["Gold"] < 75:
                sleep(0.5)
                print("You do not have enough Gold for this item.")
                sleep(1)


        #leave
        elif armor == "5":
            shopping_district()
            break
        else:
            print("Input not recognized.")
        

def weapons_shop():
    sleep(0.75)
    # some casual discrimination
    if player_stats["Class"] == "Melee":
        print("Welcome to Stabby McStabbersons Stabbing Store")
        # while true loop for deteriming what item the user wants 
        while True:
            sword = input("Stabby McStabberson offers you good deals on good sword \nYou can purchase: \n1. Shiny Sword (7 Damage, 25 Gold) \n2. Sharp Swprd (9 Damage, 40 Gold) \n3. Stabby McStabberson's Super Stabbing Sword (12 Damage, 60 Gold) \n4. Leave\n")
            
            #Sword 1
            if sword == "1" and inventory["Gold"]>=25:
                buy_stuff(25, "Shiny Sword", shiny_sword, armor=False)

            elif sword == "1" and inventory["Gold"] < 25:
                sleep(0.5)
                print("You do not have enough Gold for this Sword.")
                sleep(1)
            

            #sword 2
            elif sword == "2" and inventory["Gold"]>=40:
                buy_stuff(40, sharp_sword["weapon_name"], sharp_sword, armor=False)

            elif sword == "2" and inventory["Gold"] < 40:
                sleep(0.5)
                print("You do not have enough Gold for this Sword.")
                sleep(1)
            

            #sword 3
            elif sword == "3" and inventory["Gold"]>=60:
                buy_stuff(60, stabbies_sword["weapon_name"], stabbies_sword, armor=False)

            elif sword == "3" and inventory["Gold"] < 60:
                sleep(0.5)
                print("You do not have enough Gold for this Sword.")
                sleep(1)

            #leave
            elif sword == "4":
                shopping_district()
                break
            else:
                print("input not recognized")
    else:
        # discriminates against player depending on what class they picked
        print("Stabby McStabberson refuse to sell you sword because of your class.")
        sleep(0.75)
        print("He kicks you out.")
        shopping_district()



def town_square():
    # asks player where the want to go while in central town square
    while True:
        where_to_go = input("You are in the town square, you can \n1. Go to the Inn \n2. Go to the Shopping District \n3. Venture into the Woods \n4. Go to the Dojo\n")
        if where_to_go == "1":
            inn()
            break
        elif where_to_go == "2":
            shopping_district()
            break
        elif where_to_go == "3":
            woods()
            break
        elif where_to_go == "4":
            dojo()
        else:
            print("input not recognized, please type in the number associated with the action")


def dojo():
    # place to fight enemies for gold to get money 
    print("You enter the Dojo \nThere is only one person inside")
    x = enemy(rusty_sword, 12, 10, name=None, voice_line=None)

    if x == True:
        town_square()




def enemy(weapon, health, gold, name, voice_line):
    # main combat loop function, takes five parameters


    # Default names if the enemy isn't special
    enemy_names = ["Balbazur", "Velor", "Calluric", "Othid", "Carwel", "Ivis", "Omm", "Alathic", "Tyrak", "Zand", "Morwag", "Hari", "Gryff", "Yanthus", "Fidomar", "Elric", "Rauk", "Dasterian", "Cardon", "Anacar", "Anthrax Destroyer of Worlds", "Laybri", "Rondo", "Naeve", "Cirrus", "Heires", "Velor" ]
    
    # "Making" the enemy
    if name == None:
        enemy_inventory_and_stats = {"enemy_name": choice(enemy_names), "enemy_weapon": weapon, "health": health, "gold":gold}
    else:
        enemy_inventory_and_stats = {"enemy_name": name, "enemy_weapon": weapon, "health": health, "gold":gold}

    sleep(2)

    # prints a default voice line or the voice line passed in 
    if voice_line == None:
        print(f"I am {enemy_inventory_and_stats['enemy_name']}, you dare challenge a fighter such as myself, you will surely die.")
    else:
        print(voice_line)

    # combat loop
    while True:
        
        sleep(1)
        #player action logic
        action = input(f"You can: \n1. Attack {enemy_inventory_and_stats['enemy_name']} \n2. Use a potion \n3. Turn you weapon on yourself, ending the game\n")
        # attack action
        if action == "1":

            weapons_stats  = {}
            #dict for storing the weapons in player inventory

            for key in inventory:
                # logic getting the weapons in players inventory, puts thtem in weapon_stats

                try:
                    if inventory[key]["class"]  == "weapon":
                        sleep(0.25)
                        weapons_stats.update({inventory[key]["weapon_name"] : inventory[key]})

                except TypeError:
                    pass
            
            print("select a weapon to use by typing in the corresponding number")
    
            for key in weapons_stats:
                #prints weapon name and weapon adress for user from weapon_stats
                try:
                    print(f"{weapons_stats[key]['adress']}: {weapons_stats[key]['weapon_name']}")
                except TypeError:
                    pass
            
            #user weapon choice
            z = input()

            # part of thing to piss off players
            y = 0
            sleep(1)

            for key in weapons_stats:
                # gets weapon and subtracts damage from enemy health
                # checks if enemy health is <1 to determine of enemy is defeated
                # returns true for fun
                if z == weapons_stats[key]["adress"]:
                    enemy_inventory_and_stats["health"] = enemy_inventory_and_stats["health"] - weapons_stats[key]["Damage"]
                    print(f"You did {weapons_stats[key]['Damage']} damage to {enemy_inventory_and_stats['enemy_name']}.")
                    y = y+1
                    
                    if enemy_inventory_and_stats["health"] < 1:
                        sleep(0.75)
                        print(f"You defeated {enemy_inventory_and_stats['enemy_name']}.")
                        sleep(0.75)
                        print(f"They drop {enemy_inventory_and_stats['gold']} gold and it goes straight to your inventory!")
                        sleep(0.75)
                        inventory["Gold"] = inventory["Gold"] + enemy_inventory_and_stats["gold"]
                        return True
            if y == 0: 
                print(f"You look for a weapon you dont have and you lose your turn")
                    
        #potion action
        elif action == "2" : 
            
            # logic to determine if player has a potion, and if so how many
            potions = {}
            potion_amount = 0

            for key in inventory:

                try:
                    if inventory[key]["class"]  == "potion":
                        potions.update({inventory[key]["potion_name"] : inventory[key]})
                        potion_amount = potion_amount + 1

                except TypeError:
                    pass

            # uses potion, subtracts 1 from potion amount, sets the inventory slot the potion was in to empty
            # breaks after one potion so all potions are not removed
            if potion_amount > 0:
                player_stats["health"] = player_stats["health"] + 10

                potion_amount = potion_amount - 1 

                for key in inventory:

                    try:
                        if inventory[key]["class"]  == "potion":
                            inventory[key] = "empty"
                            break

                    except TypeError:
                        pass

                # makes sure player health after potion isn't above 15, and if so sets it back to 15
                if player_stats["health"] > player_stats["health_max"]:
                    player_stats["health"] = player_stats["health_max"]
            
                sleep(0.5)
                # prints remaining health
                print(f"You now have {player_stats['health']} health.")
                sleep(0.5)
                print(f"You have {potion_amount} health potion(s) remaining.")
                sleep(0.5)
            else:
                # part of my effort to piss off players
                print("You waste your turn looking for a non-existent potion.")
                sleep(0.5)
        
        elif action == "3":
            # print statements pretty self explanatory
            print("You turn your weapon on youself!")
            sleep(0.75)
            print("You opponent is stunned!")
            sleep(0.75)
            print("You bled out infront of a traumatized oppenent.")
            sleep(0.75)
            print("You lose.")
            sleep(3)
            exit()
        
        else:
            print("Input not recognized. You lost your turn just standing around.")
            
        # iterates through inventory looking for armor, sets "defence" to the armors defence value
        for key in inventory:
            try:
                defence = inventory[key]['defence']
                break
            except KeyError:
                defence = 0
            except TypeError:
                defence = 0

        # adjusts enemy damage 
        damage = enemy_inventory_and_stats["enemy_weapon"]['Damage'] - defence

        # prevents players from taking 0 damage or negative damage
        if damage < 1:
            damage = 1

        player_stats["health"] = player_stats["health"] - damage

        sleep(1)
        # prints enemy damage and weapoin used
        print(f"{enemy_inventory_and_stats['enemy_name']} attacks back!")
        print(f"They use a {enemy_inventory_and_stats['enemy_weapon']['weapon_name']} and deal {damage} damage")
        sleep(1)

        # closes game if player health is <1
        if player_stats["health"] < 1:
                print("You Died")
                sleep(5)
                exit()
            
        # prints remaining player health
        print(f"You now have {player_stats['health']} health remaining.")

        sleep(2)

        # end of loop, repeats until death of enemy or player


# function to add stuff to a players inventory, takes the name of the item, the dict containing the item, and whether or not the item is armor (armor takes True or False)
# function should ONLY be called after checking if the user has enough gold
def buy_stuff(price, item_name, item, armor):
    # default buy stuff
    if armor == False: 
        # adjusts gold amount, prints what the player bought and gold remaing
        gold_amount = inventory["Gold"] - price
        inventory["Gold"] = gold_amount
        print(f"You bought a {item_name}")
        sleep(0.5)
        print(f"You have {gold_amount} gold remaining")
        sleep(0.5)

        # logic to put the item in player inventory
        # the z var is used to determine if the inventory is full
        z = 0
        for key in inventory:
            if inventory[key] == "empty":
                inventory[key] = item
                z = z+1
                break

        # logic to let user select slot to fill
        if z == 0:
            while True:
                try:
                    # asks user for slot to overwtire, converts input to int, if not int, see 15 lines below, uses strip to remove whitespace
                    slot_number = int(input("Inventory Full, please slect slot to overwrite (number 1-10)\n").strip())
                    
                    # logic that deterimines if the int is valid 
                    # places item in selected slot
                    if slot_number > 0 and slot_number < 11:
                        # converts int to str so it can be apended for the slow adress
                        slot_number = str(slot_number)
                        slot_adress = "Slot " + slot_number
                        inventory[slot_adress] = item
                        break
                    else:
                        print("Input not recognized, please use a number between 1 and 10")
                        sleep(1)

                # except part of try except statement, catches value errors if a float or string is inputed
                except ValueError:
                    print("Input not recognized. Please use a number between 1-10")
                    sleep(1)                            



    if armor == True:
        # same logic as above
        gold_amount = inventory["Gold"] - price
        inventory["Gold"] = gold_amount
        print(f"You bought a {item_name}")
        sleep(0.5)
        print(f"You have {gold_amount} gold remaining")
        sleep(0.5)

        z=0
        x = 0
        # logic to replace previous set of armor, z and x vars act as bools to run other if statements
        for key in inventory:
            try:
                if inventory[key]['class'] == "armor":
                    inventory[key] = item
                    z = z+1
                    x = x + 1
                    break
            except TypeError:
                pass

        # if the x var is 0, it adds the armor to the first empty slot, sets z to 1
        if x == 0:
            for key in inventory:
                if inventory[key] == "empty":
                    inventory[key] = item
                    z = z+1
                    break
        
        # z var is used if inventory is full, same logic as above
        if z == 0:    
            while True:
                try:
                    slot_number = int(input("Inventory Full, please slect slot to overwrite (number 1-10)\n").strip())

                    if slot_number > 0 and slot_number < 11:
                        slot_number = str(slot_number)
                        slot_adress = "Slot " + slot_number
                        inventory[slot_adress] = item
                        break
                    else:
                        print("Input not recognized, please use a number between 1 and 10")
                        sleep(1)

                except ValueError:
                    print("Input not recognized. Please use a number between 1-10")
                    sleep(1)   

main()
