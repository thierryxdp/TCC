def maiores(lista, n ):
    """funcao que retorna uma lista contendo os numeros da primeira lista
       maiores que n
       
       lista, int-> lista
    """"

    list.append(lista,n)
    list.sort(lista)
    posicao_de_n = list.index(lista,n)
    
    return lista[posicao_de_n+1:]

def acima_da_media(lista):
    """funcao que retorna uma lista com as notas acima da media
    
    lista->lista
    """
    
    media= sum(lista)/len(lista)
    list.sort(lista)
    posicao_da_media = list.index(lista,media)
    
    if media in lista:
        return lista[posicao_da_media+1:]