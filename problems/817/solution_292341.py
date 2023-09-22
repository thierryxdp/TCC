def acima_da_media(lista):
    a=sum(lista)/len(lista)
    if a in lista:
        list.sort(lista)
        return lista[list.index(lista,a):]