def qtd_divisores(numero):
    lista = 0
    i = 0
    while i%numero!=0:
        lista = lista + i
        i = i + 1
    return lista