def acima_da_media(lista):
    """calculo e retorno de uma lista que mostre as notas que ficaram acima da média"""
    a=sum(lista)
    b=len(lista)
    f=list.sort(lista)
    e=list.index(lista)
    c=a//b+1
    d=lista[c:]
    return d