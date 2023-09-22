def acima_da_media(lista):
    lista.sort()
    posicao=list.index(lista,5)
    
    return lista[posicao+1:]