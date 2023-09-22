def qtd_divisores(n):
    somaDiv = 0
    for numero in range(1,n):
        if(n % numero) == 0:
            somaDiv += 1
    return somaDiv