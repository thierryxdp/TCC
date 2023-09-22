def primo():
    numero = int
    multiplo = 0
    
    for count in range(2,numero):
        if(n % count == 0):
            return True
        multiplo += 1
    
    if(multiplo == 0):
        return True
    else:
        return False