from random import randint

def game():
    status = False
    found = randint(1,100)
    attempts = 1
    while not status:
        guess = int(input("Guess a number between 1-100: "))
        print("-")

        if guess == found:
            print(f"\tCongratualtions!\n {guess} is the correct answer!\n")

            if attempts <= 3:
                print(f"""Good job getting it in right in {attempts} attempts!
                Thanks for playing!!
                """)
                status = True

            else:
                 print(f"""See if you could guess it with less than {attempts} attemps.
            Thanks for playing!
                 """)
                 status = True

        elif guess < found:
            print(f"{guess} is not quite it, try guessing higher.\n")
            attempts += 1

        else:
            print(f"{guess} is not quite it, try guessing lower.\n")
            attempts += 1

game()
