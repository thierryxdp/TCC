def qtd_divisores(n):
    i = 1
    contador = 0
    for x in range(n):
        if n%i == 0:
            contador = contador + 1
        i = i + 1
    return contador