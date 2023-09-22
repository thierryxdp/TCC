def maiores(lista1, n):
    '''função que recebe uma lista e um inteiro e retorna uma lista contendo apenas números maiores que aquele fornecido como parâmetro. list, int --> list'''
    
    lista = []

    if n in lista1:

        list.sort(lista1)
        a = list.index(lista1, n)
        x = lista1[a:]

        lista.append(x)

        lista = list.pop(lista, 0)
        
        b = list.index(lista, n) 
        list.remove(lista, n)

        return lista


    else:

        lista1.append(n)

        list.sort(lista1)
        a = list.index(lista1, n)
        x = lista1[a:]

        lista = list.pop(lista, 0)
        
        b = list.index(lista, n) 
        list.remove(lista, n)

        return lista