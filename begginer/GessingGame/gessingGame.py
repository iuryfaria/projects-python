import random

while True: # Loop for the whoele game
    print("Welcome to the Guessing Game!")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    dificult = int(input("Choose a difficulty level (1-3): "))

    if dificult == 1:
        max_number = 10
    elif dificult == 2:
        max_number = 50
    elif dificult == 3:
        max_number = 100

    secret_number = random.randint(1, max_number)
    attempts = 0

    while True: # Loop for each attempt
        guess = int(input(f"Guess a number between 1 and {max_number}: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break # Exit attempt loop

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thank you for playing! Goodbye!")
        break # Exit game loop