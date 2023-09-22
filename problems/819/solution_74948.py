def filtraMultiplos(lista,n):
    '''uma função que filtra uma lista retornadno outra lista contendo todos os elementos da lista 
    original que forem divisíveis por n.
    lista, int -> lista'''
    contador = 0
    final = []
    while contador < len(lista):
        if (lista[contador]%n=0):
            list.append(final,lista[contador])
            contador +=1
        else:   
            contador += 1
    return final