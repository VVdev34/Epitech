import random
 
def hangmanGame():
    liste = ["bronca","hardi","possibilité","cyber","pilori","retrait","poisson-perroquet","verbeux","féminisme","présomption"]
    wordChoice = random.randint(0, 10)
    finalChoice = liste[wordChoice]
    listOfLetterInWord= list(finalChoice)
    hideList = ['_'] * len(listOfLetterInWord)
    print(''.join(hideList))
    letterTried = []
    numberOfTry = 0  
 
    while "_" in hideList and numberOfTry<20:
        askingUser = input("Essaye une lettre : ").lower()
 
        if askingUser in letterTried:
            print("Oups, tu as déjà essayé cette lettre ! +3 pénalité ")
            numberOfTry += 3
            continue
 
        letterTried.append(askingUser)
        print("".join(letterTried))
 
        if askingUser in listOfLetterInWord:
            print("Bien joué !")
            for i, letter in enumerate(listOfLetterInWord):
                if listOfLetterInWord[i] == askingUser:
                    hideList[i] = letter
            print(''.join(hideList))
       
        elif askingUser == listOfLetterInWord:
            print("bravo !! ")
 
       
        else:
            print("Non ! +3 pénalité")
            numberOfTry += 3
 
gameFinished = print(input(str("felicitation ! veux-tu rejouer? ")))
if gameFinished == "oui" or gameFinished ==" Oui" or gameFinished == "OUI":
    print("c'est parti ! :) ")
    hangmanGame()
else:
    print("A bientot")
 
hangmanGame()


# creeer une liste des lettres déja joué et des nombres d'essaie a realiser
# demander une lettre a l'utilisateur
# boucler tant que le nibmre d'essaie est inférieur a nombre essaie defini, et que il y a pas de tirer dans hidden word
# test la lettre joué dans la lsite des lettres déja joué,
# ajouter la lettre dans la liste des lettes déja joué,
# tester si la lettre est dans la lite vare
#boucler avec un index et une lettre sur ton vare, si la lettre est la meme que la lettre du user, hiddenword[i]= lettre joué, print que la lettre est dans le mot, print hidden word
# else, print la lette pas la, ajouter au nombre essaie + 1
# test si il y a des tiret dans hidden word, parti fini









    

