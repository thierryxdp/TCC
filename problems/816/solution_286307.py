def maiores(lista,n):
    nova_lista = []
    i = 0
    while i < len(lista):
        if lista[i] > n:
            list.append(lista,lista[i])
            i = i + 1
    list.sort(nova_lista)
    return nova_lista