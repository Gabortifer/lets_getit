import sys, random

print("Rock, paper, scissors")
    #these variables keep track of wins, losses and ties.

wins = 0
losses = 0
ties = 0
gamesum = 0
rematch = False
bienvenido = False

while True: # main loop game
   while True:
       if rematch == True:
           print('Would love to play again!')
           rematch = False
           gamesum = 0
       else:
           while True: # aqui vemos si quiere rematch
               gamesum = gamesum + 1
               if  gamesum == 4 :
                   print('Ready to start the game!')
                   break
               elif gamesum > 4 and rematch == True:
                   break
               print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
               while True:  # The player input loop
                   print("Play!  (r)ock, (p)aper, (s)cissors or (q)uit")
                   playerMove = input()
                   if playerMove == 'q':
                       print("Thought you wanted to have fun! Well, bye")
                       sys.exit() # Quit aplication
                   if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
                       break    # Break out of Player loop
                   print('Please enter one or the other; r, s, o p. ')

               #Display what the player chooses
               if playerMove == 'r':
                   print('ROCK versus...')
               elif playerMove  == 'p':
                   print(('PAPER versus...'))
               elif playerMove == 's':
                   print('SCISSORS versus...')

               #Display what computer chooses
               randomNumber = random.randint(1,3)
               if randomNumber == 1:
                   computeMove = 'r'
                   print('ROCK')
               elif randomNumber == 2:
                   computeMove = 's'
                   print('SCISSORS')
               elif randomNumber == 3:
                   computeMove = 'p'
                   print('PAPER')

               # Display and record the win/loss/tie:
               if playerMove == computeMove:
                   print('What are the odds!')
                   ties = ties + 1
               elif playerMove == 'r' and computeMove == 's':
                   print('Rock wins over scissors!')
                   wins = wins + 1
               elif playerMove == 'p' and computeMove == 'r':
                   print('Paper traps rock')
                   wins = wins + 1
               elif playerMove == 's' and computeMove == 'p':
                   print('Scissors cut paper!')
                   wins = wins + 1
               elif playerMove == 'r' and computeMove == 'p':
                   print('Nooooo')
                   losses = losses + 1
               elif playerMove == 'p' and computeMove == 's':
                   print('Whyyyy')
                   losses = losses + 1
               elif playerMove == 's' and computeMove == 'r':
                   print('Aaah!')
                   losses = losses + 1

               print(gamesum)
               # 3 games validation
           break

       # Prompt to rematch
   while True:
       if rematch == True:
           break
       else:      # Averiguo si quiere jugar otra vez

            otrogame = ""
            print("Would you like to play again?")
            while True:
                    print("Respond (y) or (n)")
                    otrogame = input().lower()

                    # Prompt to rematch
                    if otrogame == "y":
                        print("Let's play again. Are you scared?")
                        rematch = True
                        break
                    elif otrogame == 'n':
                        print('I knew you were scared. See ya!')
                        rematch = False
                        sys.exit()
                    else:
                        print("I don't get you..")









