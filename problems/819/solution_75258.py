def filtraMultiplos(lista,n):
    '''
    Retorna todos os números da lista
    divisiveis pelo valor de n.
    list,int -> list
    '''
    i=0
    while i < len(lista):
        if lista.index(i)%n =! 0:
            lista.pop(i)
    print(lista)