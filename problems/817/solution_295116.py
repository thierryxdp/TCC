def maiores (inteiro,n):
    list.append(inteiro,n)
    list.sort(inteiro)
    ps=list.index(inteiro,n)
    lista=inteiro[ps+1:]
    return lista


def acima_da_media(lista):
    media=sum(lista)
    maiores=maiores(lista,media)
    return maiores