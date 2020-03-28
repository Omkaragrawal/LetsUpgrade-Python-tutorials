board = list("-" for i in range(1, 11))


def checkWinner():
    if (board[1] != "-" and board[2] != "-" and board[3] != "-") and (board[1] == board[2] == board[3]):  # from 1 ---> 2 ---> 3
        return board[1]
    elif (board[1] != "-" and board[4] != "-" and board[7] != "-") and (board[1] == board[4] == board[7]):  # from 1 down 4 down 5
        return board[1]
    elif (board[1] != "-" and board[5] != "-" and board[9] != "-") and (board[1] == board[5] == board[9]):  # from 1 cross 5 cross 9
        return board[1]
    elif (board[2] != "-" and board[5] != "-" and board[8] != "-") and (board[2] == board[5] == board[8]):  # from 2 down 5 down 8
        return board[2]
    elif (board[3] != "-" and board[6] != "-" and board[9] != "-") and (board[3] == board[6] == board[9]):  # from 3 down 6 down 9
        return board[2]
    elif (board[3] != "-" and board[5] != "-" and board[7] != "-") and (board[3] == board[5] == board[7]):  # from 3 cross 5 cross 7
        return board[3]
    elif (board[4] != "-" and board[5] != "-" and board[6] != "-") and (board[4] == board[5] == board[6]):  # from 4 ---> 5 ---> 6
        return board[1]
    elif (board[7] != "-" and board[8] != "-" and board[9] != "-") and (board[7] == board[8] == board[9]):  # from 7 ---> 8 ---> 9
        return board[1]
    else:
        return 0


def checkDraw():
    '''
        will return True if it is a Draw,
        will return False if it is not Draw
    '''
    checkList = []
    condition1 = board[1] == board[2]
    condition2 = board[3] == "-"
    condition3 = condition1 and condition2
    if condition3:  # [123] from 1 ---> 2 ---> 3
        checkList.append(False)
    condition1 = board[1] == board[4]
    condition2 = board[7] == "-"
    condition3 = condition1 and condition2
    if condition3:  # [147] from 1 down 4 down 7
        checkList.append(False)
    condition1 = board[1] == board[5]
    condition2 = board[9] == "-"
    condition3 = condition1 and condition2
    if condition3:  # [159] from 1 cross 5 cross 9
        checkList.append(False)
    condition1 = board[2] == board[5]
    condition2 = board[8] == '-'
    condition3 = condition1 and condition2
    if condition3:  # [258]
        checkList.append(False)
    condition1 = board[3] == board[6]
    condition2 = board[9] == "-"
    condition3 = condition1 and condition2
    if condition3:  # [369]
        checkList.append(False)
    condition1 = board[3] == board[5]
    condition2 = board[7] == "-"
    condition3 = condition1 and condition2
    if condition3:  # [357]
        checkList.append(False)
    condition1 = board[4] == board[5]
    condition2 = board[6] == '-'
    condition3 = condition1 and condition2
    if condition3:  # [456]
        checkList.append(False)
    condition1 = board[7] == board[8]
    condition2 = board[9] == '-'
    condition3 = condition1 and condition2
    if condition3:  # [789]
        checkList.append(False)

    if False in checkList:
        return False
    else:
        return True


def takeInput(isX, wrongPosition):
    '''
    isX: to request for player 1,
    wrongPosition: True if requesting  OR False if asking for First Time
    '''
    return int(input("That position is already filled please enter another location at which to place {}: ".format('X' if isX else 'O') if wrongPosition else "Please enter the position at which to place {}: ".format('X' if isX else 'O')))


def displayBoard():
    print("\t{}\t{}\t{}\n\t{}\t{}\t{}\n\t{}\t{}\t{}".format(
        board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8], board[9]))
    print("\n")


def play():
    isX = False
    for i in range(1, 10):
        isX = not isX
        displayBoard()
        if isX:
            position = takeInput(isX, False)
            if board[position] != "X" and board[position] != "O":
                board[position] = "X"
            else:
                while True:
                    position = takeInput(isX, True)
                    if board[position] != "X" and board[position] != "O":
                        board[position] = "X"
                        break
        elif not isX:
            position = takeInput(isX, False)
            if board[position] != "X" and board[position] != "O":
                board[position] = "O"
            else:
                while True:
                    position = takeInput(isX, True)
                    if board[position] != "X" and board[position] != "O":
                        board[position] = "O"
                        break
        winner = checkWinner()
        if winner != 0:
            print("Game Over winner is the {}".format(
                "First Player" if winner == "X" else "Second Player"))
            displayBoard()
            break
        elif checkDraw() :
            print("It's a Draw")
            displayBoard()
            break


print(len(board))
print("Player one will play \"X\"")
# print(board)
print("\n"*2)
play()
