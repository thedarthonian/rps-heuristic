#Imports section - Imports the needed modules
from random import *
import time
import csv
#Clears the screen on start/restart
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print ("\n*----------*    *------------* ")
print ("|   Made   |    | Rock       | ")
print ("|    by    |    |  Paper     | ")
print ("|   Darth  |    |   Scissors | ")
print ("*----------*    *------------* ")
print ()
print ("===============================")
print ("How to Play:")
print ("\n")
print ("Enter Rock, Paper, or Scissors, \nand the Computer will use a \nsimple heuristic algorithm to \nchoose it's response")
print ("===============================")
#Declaring some Variables
round = int(0)
ci="BLANK"
ui = "BLANK"
userScore=0
compScore=0
roundNum = 0
heurFile = "heuristics.csv"
#Finds persons username, just recorded along with data for future reference
print ("\nCOMPUTER: What is your username?")
name=input("YOU: ")
nameUpper=name.upper()
#Begins Porgram
while True:
     while ui != "ROCK" and ui != "PAPER" and ui != "SCISSORS":
          #Collects the users input
          ui=input("\nROUND #"+str(roundNum)+"\n=== "+nameUpper+": "+str(userScore)+" COMPUTER: "+str(compScore)+" ===\nCOMPUTER: Ok " +name + ", Pick [ROCK, PAPER, SCISSORS] or [STATS] to view stats]\n"+nameUpper+": ")
          ui=ui.upper()
          #Sets the variables the heuristic uses to 0
          r=0
          p=0
          s=0
          #Tells the user what they chose, just incase they forgot
          if ui == "ROCK":
               print ("You have chosen ROCK")
               break
          if ui == "PAPER":
               print ("You have chosen PAPER")
               break
          if ui == "SCISSORS":
               print ("You have chosen SCISSORS")
               break
          #Brings the data from the Stats file about a specific round or just prints all of the data in the heuristics file with '*'
          if ui == "STATS":
               roundStats=input("Please enter which round you'd like to view the stats for. Pick [0,1,2,3 / ALL]\n"+nameUpper+": ")
               roundStats=roundStats.upper()
               rStats = 0
               pStats = 0
               sStats = 0
               with open(heurFile,"r") as saveFile:
                    read = csv.reader(saveFile)
                    for row in read:
                         if roundStats == "*":
                              print(row)
                         elif roundStats != "*":
                              roundNumStats = row[0]
                              uiStats = row[1]
                              nameStats = row[2]
                              if int(roundNumStats) == int(roundStats) and uiStats == "ROCK":
                                   rStats = rStats + 1
                              if roundNumStats == roundStats and uiStats == "PAPER":
                                   pStats = pStats + 1
                              if roundNumStats == roundStats and uiStats == "SCISSORS":
                                   sStats = sStats + 1
                    if roundStats != "*":
                         print("=-=-= Statistics =-=-=")
                         print("Round: #"+str(roundStats))
                         print("Rock: "+str(rStats))
                         print("Paper: "+str(pStats))
                         print("Scissors: "+str(sStats))
                         if rStats > sStats and rStats > pStats:
                              print("Computer's Guess: PAPER")
                         if pStats > rStats and pStats > sStats:
                              print("Computer's Guess: SCISSORS")
                         if sStats > rStats and sStats > pStats:
                              print("Computer's Guess: ROCK")
                         else:
                              print("Computer's Guess: NOT ENOUGH DATA - Would implement random number protocol to create a response")
                   
          #If the input isn't recognises, it loops a message until an authroised input is entered.
          else:
               if ui != "STATS":
                    print ("ERROR - Please only choose ROCK, PAPER, or SCISSORS!")
          
     print("\nCOMPUTER is thinking...")
     #Gets the data from the heuristic file about the round in question
     with open(heurFile,"r") as saveFile:
          read = csv.reader(saveFile)
          for row in read:
               try:
                    roundNumf = int(row[0])
                    uif = row[1]
                    namef = row[2]
                    if roundNumf == roundNum and uif == "ROCK":
                         r = r + 1
                    if roundNumf == roundNum and uif == "PAPER":
                         p = p + 1
                    if roundNumf == roundNum and uif == "SCISSORS":
                         s = s + 1
               except IndexError:
                    print("Debug> BLANK2")
                    equalAdd = [0,1,2]
                    shuffle(equalAdd)
                    r = r + equalAdd[0]
                    p = p + equalAdd[1]
                    s = s + equalAdd[2]
     #Whichever choice has happened the most in the past, the computer will counter it
     '''print("Rock: "+str(r))
     print("Paper: "+str(p))
     print("Scissors: "+str(s))'''
     if r > s and r > p:
          ci = "PAPER"
     if p > r and p > s:
          ci = "SCISSORS"
     if s > r and s > p:
          ci = "ROCK"
     #If a clear cut winner isn't clear, we will randomly add 3, 2, and 1 to the variables and create a random choice.
     else:
          print("Debug> BLANK3")
          equalAdd = [1,2,3]
          shuffle(equalAdd)
          r = r + equalAdd[0]
          p = p + equalAdd[1]
          s = s + equalAdd[2]
          if r > s and r > p:
               ci = "PAPER"
          if p > r and p > s:
               ci = "SCISSORS"
          if s > r and s > p:
               ci = "ROCK"

     #Displays the cosmetic 'rock paper scissors' screen
     print("COMPUTER is ready\n")
     time.sleep(1)
     print("ROCK")
     time.sleep(1)
     print("  PAPER")
     time.sleep(1)
     print("    SCISSORS!\n")
     time.sleep(0.5)
     print("\n"+name + " Threw: " +ui)
     time.sleep(0.5)
     print("COMPUTER Threw: "+ci+"\n")
     time.sleep(0.5)

     #Works out and prints the winner
     if ui=="ROCK" and ci=="ROCK":
          print("--- IT'S A DRAW ---")
     if ui=="PAPER" and ci=="PAPER":
          print("--- IT'S A DRAW ---")
     if ui=="SCISSORS" and ci=="SCISSORS":
          print("--- IT'S A DRAW ---")
     if ui=="ROCK" and ci=="PAPER":
          print("--- COMPUTER WINS ---")
          compScore = compScore + 1
     if ui=="ROCK" and ci=="SCISSORS":
          print("--- YOU WIN " +nameUpper + " ---")
          userScore = userScore + 1
     if ui=="PAPER" and ci=="ROCK":
          print("--- YOU WIN " +nameUpper + " ---")
          userScore = userScore + 1
     if ui=="PAPER" and ci=="SCISSORS":
          print("--- COMPUTER WINS ---")
          compScore = compScore + 1
     if ui=="SCISSORS" and ci=="ROCK":
          print("--- COMPUTER WINS ---")
          compScore = compScore + 1
     if ui=="SCISSORS" and ci=="PAPER":
          print("--- YOU WIN " +nameUpper + " ---")
          userScore = userScore + 1

     #Adds the data to the heuristics file
     try:
          with open(heurFile,"a", newline='') as saveFile:
               write = csv.writer(saveFile)
               write.writerow([roundNum,ui,name])
               'print("Heuristics> Data added to file successfully! [",roundNum,ui,name+"]")'
     except PermissionError:
          print("ERROR - Could not save Data to Heuristics File [PermissionError]\nIf the file is currently open or in a protected location, I can't edit it!")
     #Sets up the next game then loops
     print("================================ NEW GAME ================================")
     ui = "BLANK"
     roundNum = int(roundNum) + 1
