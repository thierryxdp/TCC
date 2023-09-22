def acima_da_media(lista):
    g=sum(lista)
    y=len(lista)
    media1= g/y
    w=([i for i in lista if i>media1])
    return sorted(w)