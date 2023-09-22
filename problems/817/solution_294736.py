def maiores(lista,n):

    if n not in lista:
        list.append(lista,n)

    list.sort(lista)
    indice= list.index(lista,n)

    fatiado = lista[indice+1:]

    return fatiado

def acima_da_media(lista):
    """Função que retorna uma lista ordenada com as notas acima da média. list --> list"""
    
    media = sum(lista)/len(lista)
    
    return maiores(lista, media)