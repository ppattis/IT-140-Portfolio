#
#  Patrick D. Pattison
#  IT-140-J5082 Project Two:  Text Based Game
#  Southern Hew Hampshire University
#
#  16 June 2021 - Initial Coding...
#

#  Requirements (Simplified):  Write code for a Text Based Game as designed by Project One.
#
#  Please note that assignment requirements specified one file, although I would have
#    preferred to break this long of a program up into smaller related files.
#
#  Also note that the Hitchhiker's Guide to the Galaxy is trademark by Douglas Adams.
#    All references and quotes should be considered a work of fan-fiction, and
#    admiration.  Not plagiarism!
#

#
#  Function definition to display a help screen.
#  Although not part of requirements, I thought it adds nicely to the game...
#  NOTE:  Additional '\n' in the prints are intentional to give blank lines for readability.
def game_help():
    print("The Hitch Hikers Guide to the Galaxy Text Game")
    print("Valid Commands:")
    print("  drop <item>       Where <item> is an item name")
    print("    Drop named item.")
    print("  get <item>        Where <item> is an item name")
    print("    Pick up named item.")
    print("  go <direction>    Where <direction> can be either north, east, south, or west")
    print("    moves character in the desired direction if there is a door in that direction")
    print("  help")
    print("    Displays this help screen.")
    print("  inventory")
    print("    Display player's inventory.")
    print("  exit")
    print("    Exits game.")
    print("\n")

#
#  Function definition to display the welcome to the game.
#  NOTE:  Additional '\n' in the prints are intentional to give blank lines for readability.
def game_introduction():
    print("Welcome To\n".center(55, " "))
    print("The Hitch Hikers Guid to the Galaxy Text Game\n".center(55, " "))
    print("Adventure Awaits!\n".center(55, " "))
    print("  _____              _ _     _____            _      _ ")
    print(" |  __ \            ( ) |   |  __ \          (_)    | |")
    print(" | |  | | ___  _ __ |/| |_  | |__) |_ _ _ __  _  ___| |")
    print(" | |  | |/ _ \| '_ \  | __| |  ___/ _` | '_ \| |/ __| |")
    print(" | |__| | (_) | | | | | |_  | |  | (_| | | | | | (__|_|")
    print(" |_____/ \___/|_| |_|  \__| |_|   \__,_|_| |_|_|\___(_)")
    print("\n\n")
    game_help()

#
#  Function definition to display a goodbye screen when exiting.
#  NOTE:  Additional '\n' in the prints are intentional to give blank lines for readability.
def game_exit():
    print("\n\n")
    print("   _____         _                                         _ ")
    print("  / ____|       | |                                       | |")
    print(" | (___   ___   | |     ___  _ __   __ _    __ _ _ __   __| |")
    print("  \___ \ / _ \  | |    / _ \| '_ \ / _` |  / _` | '_ \ / _` |")
    print("  ____) | (_) | | |___| (_) | | | | (_| | | (_| | | | | (_| |")
    print(" |_____/ \___/  |______\___/|_| |_|\__, |  \__,_|_| |_|\__,_|")
    print("                                    __/ |                    ")
    print("                                   |___/                     ")
    print("     _______ _                 _           __                ")
    print("    |__   __| |               | |         / _|               ")
    print("       | |  | |__   __ _ _ __ | | _____  | |_ ___  _ __      ")
    print("       | |  | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__|     ")
    print("       | |  | | | | (_| | | | |   <\__ \ | || (_) | |        ")
    print("       |_|  |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|        ")
    print("                                                             ")
    print("                                                             ")
    print("            _ _   _   _            ______ _     _            ")
    print("           | | | | | | |          |  ____(_)   | |           ")
    print("       __ _| | | | |_| |__   ___  | |__   _ ___| |__         ")
    print("      / _` | | | | __| '_ \ / _ \ |  __| | / __| '_ \        ")
    print("     | (_| | | | | |_| | | |  __/ | |    | \__ \ | | |       ")
    print("      \__,_|_|_|  \__|_| |_|\___| |_|    |_|___/_| |_|       ")
    print("\n\n")
    print("Credits".center(55, " "))
    print("Hitch Hikers Guide to the Galaxy Copyright Douglas Adams".center(55, " "))
    print("ASCII Art thanks to https://patorjk.com/software/taag/".center(55, " "))

#
#  Function to display final boss room.

def executeBossFight(player_character):
    print("\n\n")
    print(map_information[player_character["current_location"]][0], "\n")
    print(map_information[player_character["current_location"]][1])
    print("Prostetnic Vogon Jeltz prepares the prisoners, you, to hear")
    print("his poetry recital.\n")
    if (len(player_character["inventory"]) == 7):
        print("You have managed to collect all requisite items")
        print("You have a bag to carry everything.  You have a packet")
        print("of nuts, and a couple pints of bitter to help survive and")
        print("recover from jumping through hyper-space.  You have a")
        print("Babel Fish to translate alien languages.  You got the")
        print("Electronic Sub-Etha Signaling Thumb, obviously because")
        print("you hitched a ride on the Vogon ship.  You even have")
        print("earplugs so you can avoid the dread of hearing Vogon")
        print("poetry.  But most importantly you have your towel.")
        print(" a towel has immense psychological value. For some reason,")
        print("if a strag discovers that a hitchhiker has his towel with")
        print("him, he will automatically assume that he is also in")
        print("possession of a toothbrush, washcloth, soap, tin of biscuits,")
        print("flask, compass, map, ball of string, gnat spray, wet-weather")
        print("gear, space suit etc., etc. Furthermore, the strag will then")
        print("happily lend the hitchhiker any of these or a dozen other items")
        print("that the hitchhiker might accidentally have \"lost.\" What the strag")
        print("will think is that any man who can hitch the length and breadth")
        print("of the Galaxy, rough it, slum it, struggle against terrible odds,")
        print("win through and still knows where his towel is, is clearly a man to")
        print("be reckoned with.\n")
        print("Congratulations, you have won the game!")
    else:
        print("You have failed to collect all the requisite items.  Unfortunately")
        print("you will have to suffer through the Vogon Poetry full-blast.")
        print("According to the The Hitchhiker's Guide to the Galaxy, Vogon poetry")
        print("is the third worst in the Universe. The second worst is that of the")
        print("Azgoths of Kria, and the worst is by Paula Nancy Millstone Jennings of")
        print("Sussex, who perished along with her poetry during the destruction of Earth,")
        print("ironically caused by the Vogons themselves. Vogon poetry is seen as")
        print("mild by comparison.  As your brain melts from the poetry, you wish they")
        print("would have just thrown you out of the airlock into deep space.\n")
        print("You have unfortunately lost the game...")
    input("-- Press Enter To Continue --")

if __name__ == '__main__':

    game_introduction()
    #  Variable Declarations...
    #    Player Character variable to keep track of character.
    player_character = { "name"            : "Aurthur Dent",
                         "current_location": "bedroom",
                         "inventory"       : [] }
    #    Map variable to define what room exits are valid and where they lead.
    map_valid_exits  = { "bedroom"         : { "east" : "bath_room",
                                               "down" : "living_room" },
                         "bath_room"       : { "west" : "bedroom" },
                         "living_room"     : { "up"   : "bedroom",
                                               "east": "kitchen",
                                               "down" : "front_yard" },
                         "kitchen"         : { "west" : "living_room"},
                         "front_yard"      : { "up"   : "living_room",
                                               "east" : "road"},
                         "road"            : { "west" : "front_yard",
                                               "east" : "pub",
                                               "up"   : "passageway" },
                         "pub"             : { "west" : "road"},
                         "passageway"      : { "down" : "road",
                                               "west" : "cargo_hold",
                                               "east" : "bridge" },
                         "cargo_hold"      : { "east" : "passageway" },
                         "bridge"          : { "west" : "passageway" } }
    #    Map variable for room names and descriptions.
    map_information  = { "bedroom"         : [ "Upstairs Bed Room",
                                               ("You are in your bedroom.  It is a very familiar room.  \n"
                                                "Your bed is against the wall, your dresser in the corner.  \n"
                                                "To the east is your bathroom, and down the stairs is the \n"
                                                "living room.\n")],
                         "bath_room"       : [ "Upstairs Bath Room",
                                               ("You are standing in your bathroom.  It is a normal looking \n"
                                                "bathroom.  Nothing really special about it.  To the west is \n"
                                                "your bedroom.\n") ],
                         "living_room"     : [ "Living Room",
                                               ("You are standing in your living room.  A rather plainly \n"
                                                "apportioned living room.  A couch, a chair with a foor \n"
                                                "stool, and a medium sized color T.V.  Up the stairs is \n"
                                                "your bed room, to the east is the kitchen, and down off \n"
                                                "the porch is the front yard.\n") ],
                         "kitchen"         : [ "Kitchen",
                                               ("Your kitchen is where you eat your meals, and most \n"
                                                "importantly where you make your tea.  To the west is \n"
                                                "the living room.\n") ],
                         "front_yard"      : [ "Front Yard",
                                               ("As you get to the front yard you remember that the \n"
                                                "city council wants to tear down your house to make \n"
                                                "room for a bypass.  As you lay in the mud in front \n"
                                                "of the yellow bulldozer blocking its path.  Up the \n"
                                                "stairs to the front porch is the living room and \n"
                                                "to the east is the road into town.\n") ],
                         "road"            : [ "Road into Town",
                                               ("You hear a familiar voice say \"Hello Arthur.\"  \n"
                                                "Looking up you see on of your closest friends \n"
                                                "Ford Prefect.  \"Look Arthur, are you busy?  We \n"
                                                "need to talk, over at the Horse and Groom Pub.\"  \n"
                                                "To the east the road continues on to the Horse and \n"
                                                "Groom Pub, to the west the road goes to your house, \n"
                                                "and with the help of the Electronic Sub-Etha \n"
                                                "signaling thumb is the Vogon Constructor Fleet \n"
                                                "flag ship you can hitch a ride on.\n")],
                         "pub"             : [ "The Horse and Groom Pub",
                                               ("Here's what the Encyclopedia Galatica has to say \n"
                                                "about alcohol.  It says that alcohol is a colorless \n"
                                                "volatile liquid formed by the fermentation of sugars \n"
                                                "and also notes its intoxicating effect on certain \n"
                                                "carbon-based life forms.  \"Six pints of bitter,\" \n"
                                                "Ford Prefect said to the barman of the Horse and \n"
                                                "Groom. \"And quickly please, the world's about \n"
                                                "to end.\"  To the west is the road back to your \n"
                                                "house.\n") ],
                         "passageway"      : [ "Vogon Constructor Ship Passageway",
                                               ("A stark metallic passageway.  Pipes and wires \n"
                                                "run this way and that.  Connecting some things \n"
                                                "to other things.  To the east is the cargo hold \n"
                                                "and to the west is the ships bridge.\n") ],
                         "cargo_hold"      : [ "Vogon Constructor Ship Cargo Hold",
                                               ("Dimly lit, and rather uncomfortably institutional.  \n"
                                               "To the east is the passageway.\n")],
                         "bridge"          : [ "Vogon Constructor Ship Bridge",
                                               ("The bridge of the Vogon Constructor Fleet \n"
                                                "flagship was typical for a Vogon Constructor \n"
                                                "fleet ship.  Unfortunately this particular \n"
                                                "bridge had Prostetnic Vogon Jeltz, Vogon \n"
                                                "Civil Servant and the Commander of the \n"
                                                "Vogon Constructor Fleet which was sent to \n"
                                                "destroy the planet Earth to make way for a \n"
                                                "hyper-space bypass.\n") ] }
    #    Map variable for room inventory.
    map_inventory    = { "bedroom"        : [],
                         "bath_room"       : [ "towel" ],
                         "living_room"     : [ "bag" ],
                         "kitchen"         : [ "nuts" ],
                         "front_yard"      : [ "thumb" ],
                         "road"            : [],
                         "pub"             : [ "bitters" ],
                         "passageway"      : [ "babel_fish" ],
                         "cargo_hold"      : [ "earplugs" ],
                         "bridge"          : [] }
    #    Item variable for names and descriptions.
    item_information = { "towel"           : [ "Bath Towel",
                                               "IOU Description" ],
                         "bag"             : [ "Travel Bag",
                                               "Just a regular bag to carry things in.\n" ],
                         "nuts"            : [ "Packet of Nuts",
                                               ("Vital protein that helps recover from a \n"
                                               "hyperspace jump.\n")],
                         "thumb"           : [ "Electronic Sub-Etha Signalling Thumb",
                                               ("An interesting device, worn on the finger \n"
                                                "used to hitch a ride with a passing ship.\n")],
                         "bitters"         : [ "Two Pints of Bitters",
                                               ("Used for the muscle relaxing properties.  Aids \n"
                                               "in surviving the hyperspace jump.\n")],
                         "babel_fish"      : [ "Babel Fish",
                                               ("Small, yellow and leechlike, and probably \n"
                                                "the oldest thing in the Universe.  The practical \n"
                                                "upshot is that if you stick a Babel Fish in your \n"
                                                "ear you can instantly understand anything said \n"
                                                "to you in any form of language.\n") ],
                         "earplugs"        : [ "Pair of Earplugs",
                                               "Best way to avoid having to hear Vogon Poetry.\n" ] }
    item_valid_names = { "towel"           : [ "towel",
                                               "bath towel" ],
                         "bag"             : [ "bag",
                                               "travel bag" ],
                         "nuts"            : [ "nuts",
                                               "packet",
                                               "packet of nuts" ],
                         "thumb"           : [ "thumb",
                                               "signaling thumb",
                                               "electronic thumb",
                                               "electronic sub-etha signaling thumb" ],
                         "bitters"         : [ "bitters",
                                               "pints",
                                               "two pints",
                                               "pints of bitters",
                                               "two pints of bitters" ],
                         "babel_fish"      : [ "fish",
                                               "babel fish" ],
                         "earplugs"        : [ "earplugs",
                                               "plugs" ] }

    while player_character["current_location"] != "exit":
        if player_character["current_location"] == "bridge":
            executeBossFight(player_character)
            player_character["current_location"] = "exit"
        else:
            print("\n\n")
            print(map_information[player_character["current_location"]][0], "\n")
            print(map_information[player_character["current_location"]][1])
            print("Current available commands: drop, get, go, help, inventory, and exit")
            print("Current available directions:", end=" ")
            for index, direction in enumerate(map_valid_exits[player_character["current_location"]].keys()):
                if index < (len(map_valid_exits[player_character["current_location"]]) - 1):
                    print(direction, end=", ")
                else:
                    print(direction)
            if len(map_inventory[player_character["current_location"]]) > 0:
                print("Room Inventory:")
                for index, item in enumerate(map_inventory[player_character["current_location"]]):
                    if index < (len(map_inventory[player_character["current_location"]]) - 1):
                        print(item_information[item][0], end=", ")
                    else:
                        print(item_information[item][0])
            user_input = input("\nEnter command: ")
            command_line = user_input.split()
            if command_line[0].lower() == "drop":
                #  Logic to check if player has named item, and if so drop it.
                if len(command_line) > 1:
                    named_item = ""
                    for index in range(1, len(command_line)):
                        named_item += command_line[index] + " "
                    named_item = named_item.removesuffix(" ")
                    if len(player_character["inventory"]) == 0:
                        print("You cannot drop something if you are not holding anything!")
                    else:
                        for item in player_character["inventory"]:
                            if (named_item.lower() in item_valid_names[item]):
                                player_character["inventory"].remove(item)
                                map_inventory[player_character["current_location"]].append(item.lower())
                                print("Arthur drops", item_information[item][0])
                            else:
                                print("You have to have that to drop it.")
                else:
                    print("You have to name something to drop it.")
            elif command_line[0].lower() == "get":
                #  Logic to check if named item is in the same room, and if so pick it up.
                if len(command_line) > 1:
                    named_item = ""
                    for index in range(1, len(command_line)):
                        named_item += command_line[index] + " "
                    named_item = named_item.removesuffix(" ")
                    if len(map_inventory[player_character["current_location"]]) == 0:
                        print("The room does not contain any item!")
                    else:
                        for item in map_inventory[player_character["current_location"]]:
                            if (named_item.lower() in item_valid_names[item]):
                                player_character["inventory"].append(item)
                                map_inventory[player_character["current_location"]].remove(item)
                                print("Arthur picks up", item_information[item][0])
                            else:
                                print("That item has to be in the room to pick it up.")
                else:
                    print("You have to name something to pick it up.")
            elif command_line[0].lower() == "go":
                if len(command_line) > 1:
                    if command_line[1].lower() in map_valid_exits[player_character["current_location"]].keys():
                        player_character["current_location"] = map_valid_exits[player_character["current_location"]][command_line[1].lower()]
                    else:
                        print("Either invalid direction, or unavailable direction.")
                        print("  Available directions are", end=" ")
                        for index, direction in enumerate(map_valid_exits[player_character["current_location"]].keys()):
                            if index < len(map_valid_exits[player_character["current_location"]]) - 1:
                                print(direction, end=", ")
                            else:
                                print(direction, "\n")
                else:
                    print("You have to name a direction if you want to go somewhere.")
            elif command_line[0].lower() == "inventory":
                #logic to display player inventory.
                print("\nCurrent inventory:\n")
                for item in player_character["inventory"]:
                    print(item_information[item][0].center(40, " "), item_information[item][1].center(40, " "))
                print("\n")
            elif command_line[0].lower() == "help":
                game_help()
            elif command_line[0].lower() == "exit":
                player_character["current_location"] = "exit"
            else:
                print("Invalid command.")
                print("Current available commands: go, help, and exit\n")

    game_exit()