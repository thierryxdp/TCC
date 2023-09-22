def acimada_media(lista):
    """calculo e retorno de uma lista que mostre as notas que ficaram acima da média"""
    a=sum(lista)
    b=len(lista)
    f=list.sort(lista)
    c=a//b+1
    if c in lista:
        l=list.index(lista,c)
        d=lista[l:]
        return d
    else:
        e=lista.append(c)
        g=list.sort(lista)
        k=list.index(lista,c)
        z=lista[k+1:]
        return z