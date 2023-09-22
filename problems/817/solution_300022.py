def acima_da_media(Lista):
    """
    Código que retorna uma lista ordenada com as notas da lista 
    fornecida que ficaram acima da média.
    
    :Lista -->List:
    :Return-->List:
    """
    
    Total = sum(Lista)
    Media = Total/len(Lista)
    
    Filtrado = [x for x in Lista if x >= Media]
    Filtrado.sort()
    
    if(len(Lista)==1):
        return ''
    else:
        return Filtrado