def maiores(x,n):
    list.append(x,n)
    list.sort(x)
    indice = list.index(x,n)
    del x[:(indice+1)]
    return x

def acima_da_media(x):
    qnt = len(x)
    soma = sum(x)
    media = int(soma/qnt)
    return maiores(x,media)