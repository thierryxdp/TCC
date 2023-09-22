def acima_da_media(lista):
    lista=sorted(lista)
    if len(lista)==4:
        return sum(lista)/5
    if len(lista)==5:
        return sum(lista)/6