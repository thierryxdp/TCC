def maiores(lista, n):
    y = [i for i in lista if i > n]
    acao1 = y.sort(reverse=False)
    return y

def acima_da_media(lista):
    media = sum(lista)/len(lista)
    if media in lista:
        x = maiores(lista,media)
        return x[1:]
    else:
        return maiores(lista,media)