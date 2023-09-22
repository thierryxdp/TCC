def filtraMultiplos(lista, n):
    i = 0
    lista_nova = list()
    while i < len (lista):
        teste = lista[i] % n
        if teste == 0:
        	list.append(lista_nova, lista[i])
    return lista_nova