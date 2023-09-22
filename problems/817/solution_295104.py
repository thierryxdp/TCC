def maiores(inteiro,n):
    list.append(inteiro,n)
    list.sort(inteiro)
    pos=list.index(inteiro,n)
    lista=inteiro[pos+1:]
    return lista


def acima_da_media(lista):
    media=maiores(lista)
    maiores = maiores(lista,media)
    return maiores