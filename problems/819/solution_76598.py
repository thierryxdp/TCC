def filtraMultiplos(lista,numero):
    lista_nova = []
    i = 0
    while i<len(lista):
        if lista[i]%numero == 0:
            list.insert(lista_nova,i,lista[i]):
            i = i + 1
            return lista_nova