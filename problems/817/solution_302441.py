def acima_da_media(l):
    """Pegamos os elementos da lista e tiramos a media, apos isso
    os que ficaram acima da media sao dados em lista.
    list-->list
    """
    n=sum(l)/len(l)
    d=[]
    for numeros in l:
        if numeros>n:
            d+=[numeros]            
    i=sorted(d)
    return i