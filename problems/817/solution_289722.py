def acima_da_media(lista):
    lista=sorted(lista)
    x=int(sum(lista)/len(lista))
    y=x+1
    return lista[y:]