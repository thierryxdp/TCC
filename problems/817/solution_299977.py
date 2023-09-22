def acima_da_media(Lista):
    """
    Código que retorna uma lista ordenada com as notas da lista 
    fornecida que ficaram acima da média.
    
    :Lista -->List:
    :Return-->List:
    """
    Total = sum(Lista)
    Media = Total/len(Lista)
    if x for x in Lista and x =< Media:
        return x