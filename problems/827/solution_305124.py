def qtd_divisores(n):
    divisores = list()
    lista = (n,)
    for x in lista:
        if x % n == 0:
            divisores.append(x)
    return divisores