def maiores(lista,n):
    list.extend(lista,[n])
    list.sort(lista)
    nova_lista = list()
    for i in lista:
        if i > n:
            list.extend(nova_lista,[i])
    return(nova_lista)