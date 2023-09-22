def primos(num):
    if(num % 2 == 0):
        return False
    else:
        for i in range(3, round(num/2)):
            if(num % i == 0):
                return False
    return True