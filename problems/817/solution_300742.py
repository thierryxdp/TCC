def acima_da_media(lista):
    def maiores(lista,n):
        list.append(lista,n)
        list.sort(lista)
        nyx=list.index(lista,n)
        list.remove(nyx,n)
        return nyx
    media=sum(lista)/len(lista)
    if(media in lista):
        d=maiores(lista,media)
        return d[1:]
    else:
        return maiores(lista,media)