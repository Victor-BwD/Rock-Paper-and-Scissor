from random import randint

itens = ("Rock", "Paper", "Scissor")

computer = randint(0, 2)#Computer choose a random index
player = False

while player == False:
    print("[0]Rock, [1]Paper, [2]Scissor, [3]Exit")
    playerChoice = int(input("Your choice: "))

    if playerChoice == 3:
        player = True
        print("Thank you for playing!")
    
    if playerChoice > 0 or playerChoice < 3:
        print ("--" *10)

        print("Computer plays {}".format(itens[computer]))
        print("Player plays {}".format(itens[playerChoice]))

        print ("--" *10)

        

        if playerChoice == computer:
            print('Tie')
        elif playerChoice == 0 and computer == 1:#player choose Rock and pc Paper
            print("You lose!")
        elif playerChoice == 0 and computer == 2:#player choose Rock and pc choose Scissor
            print("You win!")
        elif playerChoice == 1 and computer == 0:#player choose Paper and pc choose Rock
            print("You win!")
        elif playerChoice == 1 and computer == 2:#player choose Paper and pc choose Scissor
            print("You lose!")
        elif playerChoice == 2 and computer == 0:#player choose Scissor and pc choose Rock
            print("You lose!")
        elif playerChoice == 2 and computer == 1:#player choose Scissor and pc choose Paper
            print("You win!")
        
        print("--"*10)
        
    



    



