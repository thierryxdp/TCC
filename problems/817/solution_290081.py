def acima_da_media(lista):
    media=sum(lista)/len(lista)
    y=list.append(lista,media)
    x=list.sort(lista)
    if list.count(lista,media)==1:
        return lista[list.index(lista,media)+1:]