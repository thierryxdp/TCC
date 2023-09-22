def qtd_divisores(numero):
    lista = 0
    i = 0
    while i < numero:
        if i%numero==0:
            lista = lista + i
    return lista