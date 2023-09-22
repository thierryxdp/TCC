def qtd_divisores(n):
    lista = range(1,n)
    divisores = []
    for x in lista:
        if n%x == 0:
            list.append(divisores,x)
    return len(divisores)