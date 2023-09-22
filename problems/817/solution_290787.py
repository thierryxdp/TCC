def acima_da_media(lista):
    """calculo e retorno de uma lista que mostre as notas que ficaram acima da média"""
    a=sum(lista)
    b=len(lista)
    f=list.sort(lista)
    c=a//b+1
    l=list.index(lista,c)
    d=lista[l:]
    k=lista.append(c)
    ç=k[c:]
    if c in lista:
        return d
    else:
        return ç