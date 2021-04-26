import random 
options = ["rock", "paper", "scissors"]

def main():
    playerChoice = input("please choose rock, paper, or scissors: ")
    if playerChoice.lower() == "rock" or playerChoice.lower() == "paper" or playerChoice.lower() == "scissors":
        print("----------------------------------------------")        
    else:
        print("Sorry, please check spelling and try again.")
        
    
    compChoice = options[random.randint(0, 2)]
    if playerChoice == compChoice:
        print("It's a tie!, you chose",(playerChoice), "the computer chose",(compChoice))
    elif playerChoice.lower() == "rock":
        if compChoice.lower() == "paper":
            print("You lose!", (compChoice), "beats", (playerChoice))
        else:
            print("You win!", (playerChoice), "beats", (compChoice))
          

    elif playerChoice.lower() == "paper":
        if compChoice.lower() == "scissors":
            print("You lose!", (compChoice), "beats", (playerChoice))
        else:
            print("You win!", (playerChoice), "beats", (compChoice))


    elif playerChoice.lower() == "scissors":
        if compChoice.lower() == "rock":
            print("You lose!", (compChoice), "beats", (playerChoice))
        else:
            print("You win!", (playerChoice), "beats", (compChoice))           
          

playing = True
while playing:
    answer = input("Would you like to play again? (Y/N)")
    if answer.lower() == "yes" or answer.lower() == "y":
        main()
    elif answer.lower() == "no" or answer.lower() == "n":
        break
    else:
        print("Sorry, please check spelling and try again.")

    



