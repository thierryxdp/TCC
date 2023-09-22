def maiores(x,n):
    list.append(x,n)
    list.sort(x)
    indice = list.index(x,n)
    del x[:indice]
    if indice in x:
        list.remove(x,indice)
    return x

def acima_da_media(x):
    qnt = len(x)
    soma = sum(x)
    media = soma/qnt
    if 
    list.remove x[media]
    return maiores(x,media)