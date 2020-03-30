def isPrime(number):
    number = int(number)
    if number==0 or number==1:
        return False
    divisibilityList = list( (number%x==0) for x in range(2, int(number/2 if number/2 >= 2 else 2)))
    # print(divisibility_list)
    return True if True not in divisibilityList else False

print(isPrime("0"))
print(isPrime(1))
print(isPrime(23))
print(isPrime(77))
print(isPrime(16))
print(isPrime(98))
print(isPrime(10005))
print(isPrime(18745))
print(isPrime(2))
