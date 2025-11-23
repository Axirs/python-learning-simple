import random

def main():
    while True:
        print("\nWelcome to Rock Paper Scissor Game\n")
        user = input("Wanna play the game (y/n)? ")

        if user == "y":
            wins = 0
            computer = 0

            while True:
                try:
                    RPS = ["Rock", "Paper","Scissor"]
                    comp = random.choice(RPS)
                    choice = input("Rock, Paper, Scissor? ").lower()

                    if choice == "r" or choice == "rock":

                        if comp.lower() == "scissor":
                            print(f"The computer chooses {comp}")
                            print("You Win\n")
                            wins += 1

                            print(f"your score is {wins}, the Computer score is {computer}\n")
                            choice = input("Wanna continue(y/n)? ")
                            if choice == "n":
                                return print("Thanks for playing")

                        elif comp.lower() == "rock":
                            print(f"The computer chooses {comp}")
                            print("Draw\n")

                        elif comp.lower() == "paper":
                            print(f"The computer chooses {comp}")
                            print("You Lost\n")
                            computer += 1

                    elif choice == "p" or choice == "paper":

                        if comp.lower() == "rock":
                            print(f"The computer chooses {comp}")
                            print("You Win\n")
                            wins += 1
                           
                            choice = input("Wanna continue(y/n)? ")
                            if choice == "n":
                                print(f"your score is {wins}, the Computer score is {computer}\n")
                                return print("Thanks for playing")

                        elif comp.lower() == "paper":
                            print(f"The computer chooses {comp}")
                            print("Draw\n")

                        elif comp.lower() == "scissor":
                            print(f"The computer chooses {comp}")
                            print("You Lost\n")
                            computer += 1

                    elif choice == "s" or choice == "scissor":
                        
                        if comp.lower() == "paper":
                            print(f"The computer chooses {comp}")
                            print("You Win\n")
                            wins += 1

                            print(f"your score is {wins}, the Computer score is {computer}\n")
                            choice = input("Wanna continue(y/n)? ")
                            if choice == "n":
                                print(f"your score is {wins}, the Computer score is {computer}\n")
                                return print("Thanks for playing")
                        
                        elif comp.lower() == "rock":
                            print(f"The computer chooses {comp}")
                            print("You Lost\n")
                            computer += 1

                        elif comp.lower() == "scissor":
                            print(f"The computer chooses {comp}")
                            print("Draw\n")

                    else:
                        print("Invalid Choice")
                        print("Choose either rock, paper, scissor")

                except ValueError:
                    print("Invalid Choice")
                    print("Choose either rock, paper, scissor")

        elif user == "n":
            return print("Thanlks for playing")
        else:
            print("y/n only")

main()