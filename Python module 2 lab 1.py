import random

print("======================================")
print("       NUMBER GUESSING GAME")
print("======================================")

secret_number = random.randint(1, 100)
attempts = 0

print("I have selected a number between 1 and 100.")
print("Try to guess the number!")

while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try a bigger number.")

    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    else:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number.")
        print("Number was:", secret_number)
        print("Number of attempts:", attempts)
        break

print("======================================")
print("        GAME OVER - WELL PLAYED!")
print("======================================")
