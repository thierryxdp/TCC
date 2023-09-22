def acima_da_media(lista):
    ''' Essa função calcula a média de uma lista, voltando os valores acima da media. lista, list'''
    n = sum(lista)// len(lista)
    lista1 = n in lista 
    lista1 = lista+ [n]
    
    
    list.sort(lista)
    indice = list.index(lista,n)
    
    return lista[(indice+1):]