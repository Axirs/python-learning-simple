import random

def main():
    print("\nWelcome to Rock Paper Scissor Game\n")

    while True:
        user = input("Wanna play the game (y/n)?\n").lower()

        if user == "y":
            break
        elif user == "n":
            print("Thanks for playing")
            return
        else:
            print("y/n only\n")

    wins = 0
    round_num = 1
    computer = 0
    winner = 0

    RPS = ("r","p","s")
    rps = {"r": "Rock","p": "Paper","s": "Scissor"}


    while True:
        winner = int(input("how many score you want to win? "))
        if winner > 30:
            print("too much")
            continue
        
        print(f"\nBest of {winner}\n")

        while True:
            comp = random.choice(RPS)
            print(f"\nRound: {round_num}")
            print(f"Wins: {wins},Computer: {computer}")
            choice = input("\nRock, Paper, Scissor?(r/p/s) \n").lower()
            
            if choice not in rps:
                print("Invalid Choice")
                continue
            

            if choice == comp:
                print(f"The computer chooses {rps[comp]}")
                print(f"You also choose {rps[choice]}")
                print("Draw\n")

                round_num += 1

            elif ((choice == "p" and comp == "r") or 
                (choice == "r" and comp == "s") or 
                (choice == "s" and comp == "p")):

                print(f"The computer chooses {rps[comp]}")
                print(f"You choose {rps[choice]}")
                print("You Win\n")

                wins += 1
                round_num += 1

            else:
                print(f"The computer chooses {rps[comp]}")
                print(f"You choose {rps[choice]}")
                print("You Lost\n")

                computer += 1
                round_num += 1
            
            if wins >= winner:
                print(f"you beat the computer {winner} times")
                print("You are the overall winner")
                print("Congratulations")

                while True:
                    should_continue = input("Wanna play again?(y/n) ").lower()
                    if should_continue == "y":
                        wins = 0
                        computer = 0
                        round_num = 1
                        break
                    elif should_continue == "n":
                        print("Thanks for playing")
                        return 
                    else:
                        print("y/n only")
                
            if computer >= winner:
                print(f"The computer beat you {winner} times")
                print("Game Over")

                while True:
                    should_continue = input("Wanna play again?(y/n) ").lower()
                    if should_continue == "y":
                        wins = 0
                        computer = 0
                        round_num = 1
                        break
                    elif should_continue == "n":
                        print("Thanks for playing")
                        return 
                    else:
                        print("y/n only")
main()