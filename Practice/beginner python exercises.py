
def ageat100():
    name = input("What's your name?")
    age = input("What's is your age?")


    age100 = 2019 + 100 - int(age)
    print(name + ", you will turn 100 years old in " + str(age100))



#ageat100()
    
def oddoreven():
    number = int(input("Enter a number"))
    if number % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")

#oddoreven()


#List Comprehensions

def returnevensinlist():
    
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print([x for x in a if x%2 == 0])

def rockpaperscissors():
    player1input = input("Player 1, Choose Rock, Paper or Scissors")
    player2input = input("Player 2, Choose Rock, Paper or Scissors")

    if player1input == "rock" or player1input == "Rock" or player1input == "r":
        player1input = "a"
    elif player1input == "paper" or player1input == "Paper" or player1input == "p":
        player1input = "b"
    elif player1input == "scissors" or player1input == "Scissors" or player1input == "s":
        player1input = "c"
    else:
        print("Please enter a valid input P1")
        quit()
    
    if player2input == "rock" or player2input == "Rock" or player2input == "r":
        player2input = "a"
    elif player2input == "paper" or player2input == "Paper" or player2input == "p":
        player2input = "b"
    elif player2input == "scissors" or player2input == "Scissors" or player2input == "s":
        player2input = "c"
    else:
        print("Please enter a valid input P2")
        quit()


    if player1input == player2input:
        print("You both chose the same thing")
        quit()

        
    if player1input == "a":
        if player2input == "b":
            print("P2 Wins")
        else:
            print("P1 Wins")

    elif player1input == "b":
        if player2input == "a":
            print("P1 Wins")
        else:
            print("P2 Wins")
            
    elif player1input == "c":
        if player2input == "b":
            print("P1 Wins")
        else:
            print("P2 Wins")
    
#rockpaperscissors()


#Reversing Word Order

def reversewordorder():
    stringlist = list(input("Enter a phrase to be reversed"))
    
    newword = []
    newstringlist = []
    for i in stringlist:
        print(i)
        if i != ' ':
            newword.append(i)
        else:
            newstringlist.insert(0, newword)
            print(newstringlist)
            newword = []
    print(newstringlist)
    newstring = str(newstringlist)
    print(newstring.join(' '))
reversewordorder()
























        
        
