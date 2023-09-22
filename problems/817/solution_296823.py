def acima_da_media(lista):
    lista.sort()
    posicao=list.index(lista,5)
    
    if 5 in lista:
        return lista[posicao+1:]
    else: