def filtraMultiplos(lista,n):
    '''uma função que filtra uma lista retornadno outra lista contendo todos os elementos da lista 
    original que forem divisíveis por n.
    lista, int -> lista'''
    contador = 0
    lista1 = []
    while contador < len(lista):
        if lista1[contador]%n:
            list.append(lista1,lista1[contador])
    contador += 1
    return lista