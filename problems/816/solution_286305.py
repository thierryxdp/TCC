def maiores(lista,n):
    nova_lista = []
    i = 0
    while i < len(lista):
        if lista[i] > n:
            nova_lista = nova_lista = lista[i]
            i = i + 1
    return nova_lista