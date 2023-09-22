def acima_da_media(lista):
    """Função que retorna uma lista ordenada com as 
    notas que ficaram acima da média
    list=>list"""
    
    soma = sum(lista)
    media = soma /len(lista)
    lista.insert(0,media).sort(lista)
    
    indexdamedia = list.index(lista,media)
    listaF =lista[indexdamedia+1:]
    if listaF[0]==media:
        listaF.remove(listaF[0])
    return listaF