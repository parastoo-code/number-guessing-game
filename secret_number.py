import random

max_attempt=5
play_again="yes"

while play_again=="yes":
    the_number = random.randint(1, 100)
    won=False
    attempt = 1
    while attempt<=max_attempt:
        print(f"\nAttempt {attempt}of {max_attempt}")
        print(f"lives remaining:{max_attempt-attempt+1}")
        while True:
            try:
                guess = int(input("please Enter your guess (1-100): "))
            except ValueError:
                print("Invalid input! Please enter a whole number.")
                continue
            if guess<1 or guess>100:
                print("The number must be between 1 and 100.")
                continue
            break
        attempt+=1

        diff=abs(the_number-guess)
        if guess>the_number :
            print("Enter a smaller number")
        elif guess==the_number:
            won=True
            print("You win!")
            break
        else:
            print("Enter a bigger number")
        if diff <= 5:
            print("You're very close!")
        elif diff <= 15:
            print("You're close, but still a bit far!")
        else:
            print("You're very far!")


    if won==True:
        if attempt==1:
            print("Rank: Exeelent")
        elif attempt == 2:
            print("Rank: Very good")
        elif attempt == 3:
            print("Rank: Good")
        elif attempt == 4:
            print("Rank: Acceptable")
        elif attempt == 5:
            print("Rank: Lucky win!")
    else:
        print("You lost! The number was", the_number)

    play_again=input("Do you want to to play again?")
print("Goodbye!")

