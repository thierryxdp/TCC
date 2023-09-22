def qtd_divisores(numero):
    numeros = range(numero,0,-1)
    numeroDivisores = 0
    for i in numeros:
        if numero % i == 0:
            numeroDivisores += 1
    return numeroDivisores