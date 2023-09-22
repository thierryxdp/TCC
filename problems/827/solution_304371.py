def qtd_divisores(n):
    lista =[]
    divisores = 0
    for numero in range(1,n+1):
        if n%numero == 0:
            lista = lista + [numero]
            divisores = len(lista)
    return divisores