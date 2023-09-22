def qtd_divisores(n):
    
    if n < 0:
        return 0
    somaDiv = 0
    for numero in range(1,n):
        if(n % numero) == 0:
            somaDiv += 1
    return somaDiv