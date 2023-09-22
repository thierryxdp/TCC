def maiores(x,n):
    list.append(x,n)
    list.sort(x)
    indice = list.index(x,n)
    del x[:(indice+1)]
    return x

def acima_da_media(x):
    qnt = len(x)
    soma = sum(x)
    media = soma/qnt
    s = maiores(x,media)
    if media in x:
        y = list.index(x,media)
        del x[y]
    return