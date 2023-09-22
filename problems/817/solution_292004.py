def acima_da_media(lista):
    x = sum(lista)/len(lista)
    saida = sorted([i for i in lista if i > x])
    return saida