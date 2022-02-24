import json 
import random 
import os
from collections import Counter 

words = []
fiveletterwords = []
wordsdict = dict()

StartIO = str(input("Would you like to start? (Yes/No) "))

Comporhuman = int(input("Would you like to play or would you like a computer to solver Wordle? (1 for you, 0 for computer): "))

if StartIO == "yes" or StartIO == "y" or StartIO == "Y" or StartIO == "Yes":
    StartIO = True
else: 
    StartIO = False

print('\n')


i = 0
j = 0


filelocation = os.path.join("/Users/kille/Documents/Python\Machine Learning/WordleSolver", "fiveletterwords.json")

class Game: 
    def __init__(self, dummy):
        self.dummy = dummy

    def newDataLoad(self, new):
        if new == 1: 
            with open(filelocation) as json_file:
                global data
                data = json.load(json_file)
                print("Loaded")
                print('\n')
                global entry_list
                entry_list = list(data.items())
        else:
            print("Game Not Loaded")
        

    def chooseword(self): 
        worddecide = random.choice(entry_list)
        global choice
        choice = worddecide[1]
        print("choice word is: " + choice)
    
    def guessword(self): #ML algorithm 
        global guessword
        guessword = random.choice(entry_list)
        guessword = guessword[1]
        print('\n')
        print("guessword is: " + guessword)
    
    def MLguessword(self): 
        pointer = 0 
        WordChoices = [data]
        FirstWord = WordChoices[pointer] #Work on removing unneeded letters first
    
    def wordcolor(self, choice, guess): 
        guesscolor = dict()
        choiceword = []
        guesslist = []
        guessdict = dict()
        choicedict = dict()
        for a in choice: 
            choiceword.append(a)
        for b in guess: 
            guesslist.append(b)
        

        for idx, value in enumerate(choiceword): 
            choicedict[idx] = value
        

        for idx, value in enumerate(guesslist): 
            guessdict[idx] = value
        

        counter = 0

        lengthofword = len(guesslist)

        totalsame = 0 

        sameword = 0
        
        countsguess = Counter(guessh)
        duplicatesguess = [c for c in countsguess if countsguess[c] > 1 ]
        countschoice = Counter(choice)
        duplicateschoices = [c for c in countschoice if countschoice[c] > 1]
        
        print(duplicateschoices + duplicatesguess)
        

        while(counter < lengthofword):
            if guessdict[counter] in choicedict.values():

                totalsame += 1 
                
                if choiceword[counter] == guesslist[counter]:
                    print(f"The word at index {counter} is present in both strings in same place")
                    sameword += 1 
                    a = guessdict[counter]
                    guesscolor[a] = "green"
                
                elif len(duplicateschoices) == 0:
                    for values in duplicateschoices: 
                        dummyfunc = []
                        dummyfunc.append(values) 
                        if len(dummyfunc) > 1: 
                            killword = choiceword.index(values)
                            choiceword[killword] = "Dummy"
                            break #Append word into list after verifying its position

                else: 
                    a = guessdict[counter]
                    guesscolor[a] = "orange"
                counter += 1 
                

            else:  
                a = guessdict[counter]
                guesscolor[a] = "red"
                counter += 1

        print(guesscolor)
        print(choicedict)
        print(guessdict)
        
        print("There are " + str(totalsame) + " duplicate characters." + str(sameword) + " of them are in the same place")
    
        #print('\n'+ guessword + '\n' )

        
        if guess != choice: 
            print("Incorrect Guess")
        else: 
            print("correct guess")
            
    
dummyvariable = 0 



if StartIO == True and Comporhuman == 0:
    Repeat = int(input("How many times would you like to repeat? "))
    while i < Repeat: 
        Game(0).newDataLoad(1)
        Game(0).chooseword()
        while j < 5:
            Game(0).guessword()
            Game(0).wordcolor(choice, guessword, i, Repeat)
            
            j = j+1
        i = i + 1
        j = 0 
elif StartIO == True and Comporhuman == 1:
    p = 0
    Game(0).newDataLoad(1)
    Game(0).chooseword()
    print("You will get to play once.")
    while(p<5): 
        print('\n')
        guessh = str(input(f"input your guess no. {p + 1}: "))
        if len(guessh) == 5:
            Game(0).wordcolor(choice, guessh)
            p += 1 
        else: 
            print("input 5 letter word")

        if p == 5: 
            print("The chosen letter was: " + choice)
    


    





    
