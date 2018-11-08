import random
options=["r", "p", "s"]
choise=["Rock", "Paper", "Scissors"]
score_contu=0
SCORE_CONTP=0
TRYS=0
while True:
    USER = input("Choose your option ---> r (Rock) ---> p (Paper) ---> s (Scissors): ")
    X = random.choice(options)
    if USER == 'r':
        print("Your Choice: %s "%choise[0])  
    elif USER == 'p':
        print("Your Choice: %s "%choise[1])
    elif USER == 's':
        print("Your Choice: %s "%choise[2])
    if USER == X:
        TRYS += 1
        print("Try Again")
        print("Socores: %d and %d"%(score_contu, SCORE_CONTP))
    elif USER == 'p' and X == 'r':
        TRYS += 1
        print("YOU WIN")
        score_contu += 1
        print("Socores: %d and %d"%(score_contu, SCORE_CONTP))
    elif USER == 'r' and X == 's':
        TRYS += 1
        print("YOU WIN")
        score_contu += 1
        print("Socores: %d and %d"%(score_contu, SCORE_CONTP))
    elif USER == 's' and X == 'p':
        TRYS += 1
        print("YOU WIN")
        score_contu += 1
        print("Socores: %d and %d"%(score_contu, SCORE_CONTP))
    else:
        TRYS += 1
        print("Computer WIN")    
        SCORE_CONTP += 1
        print("Socores: %d and %d"%(score_contu, SCORE_CONTP))
    if score_contu == 2:
        print("CONGRATULATIONS!!! YOU ARE THE WINER")
        print("FINAL SCORE:%d and &d"%(score_contu, SCORE_CONTP))
        break    
    elif SCORE_CONTP == 2:
        print("COMPUTER BEATS YOU")
        print("FINAL SCORE: %d and %d "%(score_contu, SCORE_CONTP))
        break
    elif TRYS == 3:
        print("You reached Three intentd----Nobody WIN try again")
        break
    
