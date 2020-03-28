input_list = list(int(element) for element in input(
    "Enter the contents of the list (please give a space as a seperator in each content )").split())
contentToCheck = [1, 1, 5]
print(input_list)

def checkForContents(toCheckList, valueToCheck=contentToCheck[0], positionFrom=0):
    try:
        indexAt = input_list.index(valueToCheck, positionFrom)
        contentToCheck.remove(valueToCheck)
        condition = len(contentToCheck) <= 0
        if condition:
            print("Should print for true")
            return True
        else:
            checkForContents(toCheckList, contentToCheck[0], indexAt + 1)
    except Exception as error:
        print(error)
        return False

print(checkForContents(input_list))
#print("it's a Match" if checkForContents(input_list) else "it's Gone")
