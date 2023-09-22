def acima_da_media(lista):
    lista=sorted(lista)
    a=len(lista)
    if a%2==0:
        return lista[a//2:]
    else:
        return lista[a//2+1:]