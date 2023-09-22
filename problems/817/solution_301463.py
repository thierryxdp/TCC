def acima_da_media(lista):
    '''
    list.append(lista)
     a = len(inteiros)
    b = list.index(inteiros,n)
    return inteiros[b+1:a]
    '''
    list.sort(lista)
    a = len(lista)
    b = list.index(lista,5,6,7,8,9,10)
    
    return lista[b:a]