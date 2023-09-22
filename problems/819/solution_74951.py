def filtraMultiplos(lista,n):
    '''uma função que filtra uma lista retornadno outra lista contendo todos os elementos da lista 
    original que forem divisíveis por n.
    lista, int -> lista'''
    contador = 0
    lista = []
    while contador < len(lista):
        if lista[contador]%n:
            list.append(lista,lista[contador])
    contador += 1
    return lista