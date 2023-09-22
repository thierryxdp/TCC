def divisor(num):
    for i in range(1, int(num/2+1)):
        if num % i == 0: 
           return i
    return num