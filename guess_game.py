import random
n=0
secret_number=random.randint(1,100)
print("welcome to the word of guess")
while True:
    guess=int(input("guess a number between 1 to 100:"))
    n=n+1
    if guess==secret_number:
        print("congratulation! you guessed it right","in",n,"attempts")
        break
    elif guess<secret_number:
        print("too low try again!")
    else:
        print("too high try again!")