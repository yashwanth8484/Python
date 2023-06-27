import random

toprange=input("type a number: ")

if toprange.isdigit():
    toprange=int(toprange)
    if toprange<=0:
        print("please enter a number more than 0")
        quit()
else:
    print("plz type a number next time....")
    quit()

r = random.randrange(0,toprange)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess--")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("plz type a number next time....")
        continue

    if user_guess == r:
        print(" yeah u got it..")
        break
    else:
        print("No, sry u got it wrong")
print("you got it in", guesses, "guesses")