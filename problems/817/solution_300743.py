def acima_da_media(lista):
    def maiores(lista,n):
        list.append(lista,n)
        list.sort(lista)
        nyx=list.index(lista,n)
        return lista[nyx+1:]
    media=sum(lista)/len(lista)
    if(media in lista):
        d=maiores(lista,media)
        return d[1:]
    else:
        return maiores(lista,media)