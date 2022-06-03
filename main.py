import random
print("Welcome to Rock-Paper-Scissors game ")
# print("***___***___***___***___***___***___***___***___***")
# print("___***___***___***___***___***___***___***___***___")
# print("***___***___***___***___***___***___***___***___***")
while 1:
    print("\n***INSTRUCTION***\nEnter R for Rock \nEnter P for Paper \nEnter S for Scissors\nEnter H for help\nEnter X to quit\n")
    cpu = random.choice(["R", "P", "S"])
    user = input("Enter your choice >> ")

    cpu = cpu.upper()
    user = user.upper()

    if ((user == "R")  or (user == "P") or (user == "S")):
        game = str(user)+str(cpu)
        user_v = ("Rock" if user == "R" else "Paper" if user == "P" else "Scisors")
        cpu_v = ("Rock" if cpu == "R" else "Paper" if user == "P" else "Scisors")

        if ((game == "RS") or (game == "PR") or (game == "SP")):
            #user wins
            print(f"Player ({user_v}) : CPU ({cpu_v})")
            print("\nUser Wins\nGame over :)")
            exit()
        elif ((game == "SR") or (game == "RP") or (game == "PS")):
            #cpu wins
            print(f"Player ({user_v}) : CPU ({cpu_v})")
            print("CPU Wins\nGame over :(")
            exit()
        else:
            #tie
            print(f"Player ({user_v}) : CPU ({cpu_v})")
            print("\nIt's a Tie :| \nLet's try again")
    elif (user == 'H'):
        print("\n***GAME HELP***")
        print("Rock beats Scissors\nPaper beats Rock\nScissors beats Paper\n\n")
    elif (user == "X"):
        exit()
    else:
        print("Invalid command. Try again \n'X' to quit\n\n")