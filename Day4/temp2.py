board = []


def checkDraw():
    '''
        will return True if it is a Draw,
        will return False if it is not Draw
    '''
    checkList = []

    if (board[1] == board[2]) and (board[3] != "-" and board):  # [123] from 1 ---> 2 ---> 3
        checkList.append(True)
    elif (board[1] == board[4]) and board[7] != "-":  # [147] from 1 down 4 down 7
        checkList.append(True)
    elif (board[1] == board[5]) and board[9] != "-":  # [159] from 1 cross 5 cross 9
        checkList.append(True)

    if (board[2] == board[5]) and board[8] != '-':  # [258]
        checkList.append(True)
    elif (board[3] == board[6]) and board[9] != "-":  # [369]
        checkList.append(True)
    elif (board[3] == board[5]) and board[7] != "-":  # [357]
        checkList.append(True)

    if (board[4] == board[5]) and board[6] != '-':  # [456]
        checkList.append(True)
    if (board[7] == board[8]) and board[9] != '-':  # [789]
        checkList.append(True)

    if len(checkList) != 0:
        return False
    else:
        return True
