import random

secret_number =  random.randint(1,101)
tries = 0
while tries < 10:
  tries += 1
  guess = int(input(' enter a number: '))    
  if guess < secret_number:
    print(str(10 - tries) + ' Attempts left : Your guess is lower.. Try Again')
  elif guess > secret_number:
    print(str(10 - tries) + ' Attempts left : Your guess is higher.. Try Again')
  else: 
    print( "You guessed right with " + str(10 - tries) + ' attempts stil left!')
    break

if guess != secret_number and tries == 10:
  print('Sorry! The correct number was: ' ,secret_number)
