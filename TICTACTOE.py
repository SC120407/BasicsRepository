#Tic Tac Toe
import random
print("Welcome to Tic Tac Toe")
print("------------------------")

#Making gameboard "slots"
possible_num = [1,2,3,4,5,6,7,8,9]
#Making two-dimensional gameboard array (Grouping the individual slots together)
Game_Board = [[1,2,3],[4,5,6],[7,8,9]]

#Making Rows and columns of the gameboard to be print
rows = 3
columns = 3

def printGameboard():
    #Defining rows of the gameboard
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        #Printing columns of the gameboard
        for y in range(columns):
            print("", Game_Board[x][y], end=" |")
    print("\n+---+---+---+")

printGameboard()

def ModifyArray(num, Insertmove):
    num -= 1
    if (num == 0):
        Game_Board[0][0] = Insertmove
    elif (num == 1):
        Game_Board[0][1] = Insertmove
    elif (num == 2):
        Game_Board[0][2] = Insertmove
    elif (num == 3):
        Game_Board[1][0] = Insertmove
    elif (num == 4):
        Game_Board[1][1] = Insertmove
    elif (num == 5):
        Game_Board[1][2] = Insertmove
    elif (num == 6):
        Game_Board[2][0] = Insertmove
    elif (num == 7):
        Game_Board[2][1] = Insertmove
    elif (num == 8):
        Game_Board[2][2] = Insertmove

def CheckWinner(Game_Board):
    #X-axis win
    if(Game_Board[0][0] == "X" and Game_Board[1][0] == "X" and Game_Board[2][0] == "X"):
        print("X has won")
        quit()
        return "X"
    elif(Game_Board[0][0] == "O" and Game_Board[1][0] == "O" and Game_Board[2][0] == "O"):
        print("O has won")
        quit()
        return "O"
    elif(Game_Board[0][1] == "X" and Game_Board[1][1] == "X" and Game_Board[2][1] == "X"):
        print("X has won")
        quit()
        return "X"
    elif(Game_Board[0][1] == "O" and Game_Board[1][1] == "O" and Game_Board[2][1] == "O"):
        print("O has won")
        quit()
        return "O"
    elif(Game_Board[0][2] == "X" and Game_Board[1][2] == "X" and Game_Board[2][2] == "X"):
        print("X has won")
        quit()
        return "X"
    elif(Game_Board[0][2] == "O" and Game_Board[1][2] == "O" and Game_Board[2][2] == "O"):
        print("O has won")
        quit()
        return "O"
    #Y-axis win
    if(Game_Board[0][0] == "X" and Game_Board[0][1] == "X" and Game_Board[0][2] == "X"):
        print("X has won")
        quit()
        return "X"
    elif(Game_Board[0][0] == "O" and Game_Board[0][1] == "O" and Game_Board[0][2] == "O"):
        print("O has won")
        quit()
        return "O"
    elif(Game_Board[1][0] == "X" and Game_Board[1][1] == "X" and Game_Board[1][2] == "X"):
        print("X has won")
        quit()
        return "X"
    elif(Game_Board[1][0] == "O" and Game_Board[1][1] == "O" and Game_Board[1][2] == "O"):
        print("O has won")
        quit()
        return "O"
    elif(Game_Board[2][0] == "X" and Game_Board[2][1] == "X" and Game_Board[2][2] == "X"):
        print("X has won")
        quit()
        return "X"
    elif(Game_Board[2][0] == "O" and Game_Board[2][1] == "O" and Game_Board[2][2] == "O"):
        print("O has won")
        quit()
        return "O"
    #Cross Win
    if(Game_Board[0][0] == "X" and Game_Board[1][1] == "X" and Game_Board[2][2] == "X"):
        print("X has won")
        quit()
        return "X"
    elif(Game_Board[0][0] == "O" and Game_Board[1][1] == "O" and Game_Board[2][2] == "O"):
        print("O has won")
        quit()
        return "O"
    if(Game_Board[2][0] == "X" and Game_Board[1][1] == "X" and Game_Board[0][2] == "X"):
        print("X has won")
        quit()
        return "X"
    elif(Game_Board[2][0] == "O" and Game_Board[1][1] == "O" and Game_Board[0][2] == "O"):
        print("O has won")
        quit()
        return "O"

leaveloop = False
turnCounter = 0

while (leaveloop == False):
    #It is player's turn
    CheckWinner(Game_Board)
    if(turnCounter % 2 ==1):
        printGameboard()
        #Enter number and see if it is valid
        numberPicked = int(input("\n Enter the number: "))
        if(numberPicked <= 9 and numberPicked >= 1 and numberPicked in possible_num):
            ModifyArray(numberPicked, "X")
            possible_num.remove(numberPicked)
        #If number is invalid
        else:
            print("Invalid input. Try again")
            continue
            printGameboard()

        turnCounter += 1
    #It is computer's turn
    else:
        while(True):
        #Computer choice
            cpuchoice = random.choice(possible_num)
            print(f"\ncpuchoice: {cpuchoice}" )
            if(cpuchoice in possible_num):
                ModifyArray(cpuchoice, "O")
                possible_num.remove(cpuchoice)
                turnCounter += 1
                break


