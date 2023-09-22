def carros(n):
    
    if (n%5==0):

        return int(n/5)

    elif (n%5 != 0):

        return int((n//5) + 1)