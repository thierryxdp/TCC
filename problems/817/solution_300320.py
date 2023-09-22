def acima_da_media(lista):
    ''' Essa função calcula a média de uma lista, voltando os valores acima da media. lista, list'''
    n = sum(lista)// len(lista)
    n_lista = [n]
    lista1 = lista+ n_lista
    list.sort(lista1)
    indice = list.index(lista1,n)
    
    return lista1[(indice+1):]