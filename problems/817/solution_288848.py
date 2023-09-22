def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    p=list.index(lista,n)
    maiores=lista[p+1:]
    return maiores

def acima_da_media(notas):
    soma=sum(notas)
    media=soma/len(notas)
    acima = maiores(notas,media)
    if media in acima:
        list.remove(acima,media)
    return acima