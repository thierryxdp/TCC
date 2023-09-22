def acima_da_media(lista_numero):
    new=[]
    start=0
    while start < len(lista_numero):
        if lista_numero[start] > 5:
            new = new + [lista_numero[start],]
        start = start + 1
    list.sort(new)
    return new