def qtd_divisores(x):
    lista = []
    lista1 = list(range(1, x+1))
    for i in lista1:
        if x % i == 0:
            lista = lista + [i]
    return lista