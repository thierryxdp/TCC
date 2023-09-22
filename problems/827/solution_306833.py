def qtd_divisores(n):
    numeros = ''
    for i in range(10):
        if n%i == 0:
            numeros = numeros + i
    return numeros