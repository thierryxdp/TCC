def qtd_divisores(n):
    numeros = ''
    for i in range(1,n+1):
        if n%i == 0:
            numeros = numeros + str(i) + ','
    return len(numeros)