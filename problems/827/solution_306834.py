def qtd_divisores(n):
    numeros = ''
    i = 1
    while i in range(1,10):
        if n%i == 0:
            numeros = numeros + i
    return numeros