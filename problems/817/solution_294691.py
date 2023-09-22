def acima_da_media(lista):
    lista=sorted(lista)
    x=len(lista)
    m=x//2
    if (x%2)!=0:
        m=(x+1)/2
    return lista[m:]