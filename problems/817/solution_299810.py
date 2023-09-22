def acima_da_media(lista_numero):
    new=[]
    start=0
    M=sum(lista_numero)/len(lista_numero)
    while start < len(lista_numero):
        if lista_numero[start] > M:
            new = new + [lista_numero[start],]
        start = start + 1
    list.sort(new)
    return new