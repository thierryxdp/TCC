def acima_da_media(lista):
    ''' Essa função calcula a média de uma lista, voltando os valores acima da media. lista, list'''
    n = sum(lista)// len(lista)
    lista1 = lista
    if n in lista:
        return lista1
    else:
        return lista1 + [n]
    
    
    
    list.sort(lista1)
    indice = list.index(lista1,n)
    
    return lista1[(indice+1):]