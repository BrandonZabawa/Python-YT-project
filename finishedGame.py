import random  

def rollPairDice():
  return random.randint(1, 6) + random.randint(0, 6)

def userMoney(enterMoney = int(input("Place your bets here:\n"))):
  return enterMoney

def houseBet(houseWager = random.randint(0,25000)):
  return houseWager

def moneyPot():
  personalMoney, houseMoney = userMoney(), houseBet()
  pot = personalMoney + houseMoney
  return pot


def moneyLost(losingCheddar = random.randint(0,1500)):
  return losingCheddar


def playOrstay(userDecision=input("play or stay?\n")):
  return userDecision

def myGame(randomNum=rollPairDice(), totalPot=moneyPot(), multiplier=3, guess=-1, decision=playOrstay()):

  guessChecker = 0
  highChecker = 0
  lowChecker = 0


  if decision == "play":
    
    print("Welcome to guess the di.")
    print("The game which you can legit clear your college debt!")
    print("If you don't get it right you don't get a lot of money.")
    print("Guess it right you'll get a boatload of money!")

    while guess != randomNum and totalPot > 0 and highChecker!=10:
      guessChecker = guessChecker + 1
      guessNum = int(input("What is your guess\n"))
      
      if guessNum<randomNum:
        lowChecker = lowChecker + 1
        totalPot = totalPot - moneyLost()
        
        if totalPot > 0:
          print("Your guess is too low.", "you guessed:", lowChecker, "times.")
          print("you guessed wrong you now have $", totalPot)
        else:
          print("You lost all your money!")
          break

      elif guessNum > randomNum:
        highChecker = highChecker + 1
        totalPot = totalPot - moneyLost()
        
        if totalPot > 0:
            print("Your guess is too high. You have made", highChecker, "guesses that were too high.")
            print("you guessed wrong you now have $", totalPot)
            if highChecker >= 10:
              print("Sorry you lost by making too many high guesses.\nThe correct number was", randomNum, end=".")

      elif guessNum == randomNum:
        totalPot = totalPot * multiplier
        
        print("Congrats, you got the number in", guessChecker, "guesses, of which", highChecker, "were to high")
        print("you guessed right you now have $", totalPot)
        
        highChecker = 0
        decider2 = input("play or stay?\n")
        
        if decider2 == "stay":
          print("You chose to stay. This is your money: ", totalPot)
          break
  
  elif decision=="stay":
    print("Nevermind game over, heres your money back:")
    print(userMoney())

    
def secondGame(store=myGame()):
  return store

secondGame()
