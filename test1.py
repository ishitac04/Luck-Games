score=0
while True:
     
    print()

    def pickanumber():
        print()
        print("In this game, you will guess a number between 1-5. A random number will be generated by the computer. If you're number is the same as the generated number, you win!")
        import random
        print()

        number=random.randint(1,5)
        choice=int(input("Enter your chosen number (between 1-5): "))
        print()

        print("CHOSEN NUMBER: "+str(choice))
        print("GENERATED NUMBER: "+str(number))
        print()

        if choice == number:
            print("You win! ")
            return 1
        else:
            print("You lose :(")
        print()

    def rockpaperscissors():
        print()
        print("In this game, you will choose rock, paper or scissors. The computer will then choose rock, paper or scissors. Rock beats scissors, paper beats rock, scissors beat paper.")
        import random
        print()
        sign="hello"

        number=random.randint(1,3)
        choice=input("Enter your chosen sign (rock, paper or scissors): ")
        if number==1:
            sign="rock"
        elif number==2:
            sign="paper"
        else:
            sign="scissors"
        print()

        print("YOUR CHOSEN SIGN: "+str(choice.lower()))
        print("GENERATED SIGN: "+str(sign))
        print()

        if choice.lower() == "rock" and sign=="paper":
            print("The computer wins! ")
        elif choice.lower() == "paper" and sign=="scissors":
            print("The computer wins! ")
        elif choice.lower() == "scissors" and sign=="rock":
            print("The computer wins!")
        elif choice.lower() == "rock" and sign=="scissors":
            print("You win!")
            return 1
        elif choice.lower() == "paper" and sign=="rock":
            print("You win!")
            return 1
        elif choice.lower() == "scissors" and sign=="paper":
            print("You win!")
            return 1
        else:
            print("Its a tie!")
        print()
    
    def flipacoin():
        print()
        print("In this game, you will guess whether the coin lands on heads or tails. If you are right, you win! ")
        import random
        number=random.randint(1,2)
        if number==1:
            coin="Heads"
        else:
            coin="Tails"
        choice=input("Enter your guess: ")
        if choice.lower()=="heads" and number==1:
            print("You win!")
            return 1
        elif choice.lower()=="tails" and number == 2:
            print("You win!")
            return 1
        else:
            print("You lose")

    print("LUCK GAMES:")
    print("1 - Guess The Number")
    print("2 - Rock Paper Scissors")
    print("3 - Flip a Coin")
    choice=input("Choose which game you want to play! ")
    if choice=="1":
        increase=pickanumber()
    elif choice=="2":
        increase=rockpaperscissors()
    elif choice=="3":
        increase=flipacoin()
    
    if increase==1:
            score=score+1
    print("Your current score is "+str(score)+".")
    again=input("Do you want to play again? ")
    if again.lower()=="yes":
        pass
    else:
        break