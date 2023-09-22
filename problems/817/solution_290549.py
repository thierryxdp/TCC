def acima_da_media(lista):
    """calculo e retorno de uma lista que mostre as notas que ficaram acima da média"""
    a=sum(lista)
    b=len(lista)
    f=list.sort(lista)
    c=a//b+2
    f=list.index(lista,c)
    d=lista[f:]
    return d