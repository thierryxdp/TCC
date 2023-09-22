def qtd_divisores(numero):
    lista = ()
    i = 0
    while i < numero:
        if i%numero==0:
            lista = lista + (i,)
        i = i + 1
    return len(lista)