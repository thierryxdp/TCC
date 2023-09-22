def primo(n):
    ''''''
    contador = 1
    metade = n//2
    for i in range (1, metade+1):
        if((n % i) == 0):
            return contador +=1
    if contador == 2:
        return True
    else:
        return False