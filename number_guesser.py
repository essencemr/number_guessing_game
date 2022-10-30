import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Uh Oh! Your number must be larger than 0")
        quit()
else:
    print("Uh oh! That's not a number")
    quit()

    

random_number = random.randrange(top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        
        continue
    if user_guess == random_number:
        print("Eureka! The random number was:", random_number,)
        break


    elif user_guess > random_number:
        print("You are above the number.")
    else:
        print("You are below the number.")

print("You got it in", guesses, "guesses")
