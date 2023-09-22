def filtraMultiplos (lista,n):
    '''recebe uma lista e um número n, e retorna uma nova lista com os múltiplos de n'''
    lista2 = []
    i = 0
    while i <len(lista):
        if lista[i]%n==0:
            lista2 = lista2+(lista[i],)
            i = i+1
    return lista2