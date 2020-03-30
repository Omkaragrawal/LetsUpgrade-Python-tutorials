'''
    is_prime(): returns True if it is a Prime Number, else False if not a Prime Number
'''

def is_prime(number):
    '''
        number: The number to be checked

        returns True if it is a Prime Number, else False if not a Prime Number
    '''
    number = int(number)
    if number in (0, 1):
        return False
    divisibility_list = list((number%x == 0) for x in range(2, int(number/2 if number/2 >= 2 else 2)))
    # print(divisibility_list)
    return bool(True not in divisibility_list)

print(is_prime("0"))
print(is_prime(1))
print(is_prime(23))
print(is_prime(77))
print(is_prime(16))
print(is_prime(98))
print(is_prime(10005))
print(is_prime(18745))
print(is_prime(2))
