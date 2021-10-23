#
#  Patrick D. Pattison
#  IT-140-J5082 6-4 Milestone Assignment: Moving Between Rooms
#  Southern Hew Hampshire University
#
#  10 June 2021 - Initial Coding...
#

#  Requirements (Simplified):  Write code that will display a simplified version
#                              of the Dragon text game, and take user input to
#                              move the adventurer from room to room, and allow
#                              the user to exit the game.  Room names,
#                              descriptions, and the rooms dict variable were
#                              provided by the assignment.
#

#
#  Global game variable declarations...

#  Variable to keep track of current room.
current_room = "Cellar"

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'south': 'Bedroom'},
        'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
        'Cellar': {'west': 'Bedroom'}
    }

#  A dictionary for the room descriptions...
room_descriptions = {
    "Great Hall": "In the Great Hall\n",
    "Bedroom": "In the Bedroom\n",
    "Cellar": "In the Cellar\n"
}

#
#  Function definition to display a help screen.
#  Although not part of requirements, I thought it adds nicely to the game...
#  NOTE:  Additional '\n' in the prints are intentional to give blank lines for readability.
def game_help():
    print("Simplified Dragon Game Help")
    print("Valid Commands:")
    print("  go <direction>    Where <direction> can be either north, east, south, or west")
    print("    moves character in the desired direction if there is a door in that direction")
    print("  help")
    print("    Displays this help screen.")
    print("  exit")
    print("    Exits game.")
    print("\n")

#
#  Function definition to display the welcome to the game.
#  NOTE:  Additional '\n' in the prints are intentional to give blank lines for readability.
def game_introduction():
    print("Welcome to the Simplified Dragon Text Game\n")
    print("Adventure (At least a simplified version) Awaits!\n")
    game_help()

#
#  Function definition to display a goodbye screen when exiting.
#  NOTE:  Additional '\n' in the prints are intentional to give blank lines for readability.
def game_exit():
    print("\n\n")
    print("Farewell adventurer.  Thank you for playing.\n")
    print("I hope you got simplified enjoyment from your time here!")

#
#  Main Game Loop
while current_room != "Exit":

    print(current_room, "\n")
    print(room_descriptions[current_room])
    print("Current available commands: go, help, and exit")
    print("Current available directions:", end=" ")
    for index, direction in enumerate(rooms[current_room].keys()):
        if index < len(rooms[current_room]) - 1:
            print(direction, end=", ")
        else:
            print(direction)
    user_input = input("\nEnter command: ")
    command_line = user_input.split()
    if command_line[0].lower() == "go":
        if command_line[1].lower() in  rooms[current_room].keys():
            current_room = rooms[current_room][command_line[1].lower()]
        else:
            print("Either invalid direction, or unavailable direction.")
            print("  Available directions are", end=" ")
            for index, direction in enumerate(rooms[current_room].keys()):
                if index < len(rooms[current_room]) - 1:
                    print(direction, end=", ")
                else:
                    print(direction, "\n")
    elif command_line[0].lower() == "help":
        game_help()
    elif command_line[0].lower() == "exit":
        current_room = "Exit"
    else:
        print("Invalid command.")
        print("Current available commands: go, help, and exit\n")
game_exit()

