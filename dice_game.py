import random

def dice1():
    return random.randint(1,6)

def dice2():
    return random.randint(1,6)

def main():
    while True:
        try:
            while True:
                print("\nWELCOME TO DICE GAME\n")
                choice = input("Do you want to play dice game (y/n)? ").lower()
                if choice == "y":
                    while True:
                        dice_number = int(input("\nOne dice game or two dice game?\nChoose 1 or 2\n"))
                        if dice_number == 1:
                            try:
                                while True:
                                    attempts = int(input("how many attempts? "))
                                    for i in range(attempts):
                                        dice = dice1()
                                        print(f"attempts: {i + 1}, dice: {dice}")
                                    choice = input("\nwanna continue?(y/n) \n"
                                    "or choose number of dice(c) \n").lower()
                                    if choice == "n":
                                        return print("thanks for playing")
                                    elif choice == "c":
                                        print("going back\n")
                                        break                               
                            except ValueError:
                                print("Invalid")    
                        elif dice_number == 2:
                            try:
                                while True:
                                    attempts = int(input("how many attempts? "))
                                    for i in range(attempts):
                                        dice_1 = dice1()
                                        dice_2 = dice2()
                                        print(f"attempts: {i + 1}, dice 1: {dice_1}, dice 2: {dice_2}")
                                    choice = input("\nwanna continue?(y/n) \n"
                                    "or choose number of dice(c) \n").lower()
                                    if choice == "n":
                                        return "thanks for playing"
                                    elif choice == "c":
                                        print("going back\n")
                                        break                               
                            except ValueError:
                                print("Invalid")  
                        else:
                            print("invalid choice")
                elif choice == "n":
                    return "Thanks for playing"
                else:
                    print('only y/n')
        except ValueError:
            print("invalid choice")
main()