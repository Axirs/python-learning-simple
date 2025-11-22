import random

def guess_num(n):
    return random.randint(1, n)

def main():
    while True:
        print('\nWELCOME TO GUESSING NUMBERS GAME\n')
        choice = input("Wanna play the game (y/n)? ").lower()
        if choice == "y":
            try:
                level = int(input("Upto what number do you want to guess? "))
                secret_number = guess_num(level)
                guess_count = 0
                while True:
                    try:
                        guess = int(input(f"Guess number 1 up to {level}\n"))
                        guess_count += 1
                        if guess == secret_number:
                            print(f"You guess the number {guess} right")
                            print("HOORAYYY")
                            choice = input("Wanna play again (y/n)? ").lower()
                            if choice == "n":
                                return print("Thanks for playing")
                            elif choice == "y":
                                break 
                        else:
                            print("Wrong")
                            if guess_count >= 3:
                                choice = input("Want hint? (y/n) ").lower()
                                if choice == "y":
                                    if guess > secret_number:
                                        print("\nLESSER\n")
                                    elif guess < secret_number:
                                        print("\nGREATER\n")
                    except ValueError:
                        print("Invalid guess input. Please enter a number.")
            except ValueError:
                print("Invalid level input. Please enter a number.")
        elif choice == "n":
            return print("Thanks for playing")
        else:
            print("Invalid Choice. Please enter y or n.")

main()