def qtd_divisores(x):
    ''''''
    contador = 0
    for i in range(1, x+1):
        if (x % i) == 0:
            contador +=4
    return contador