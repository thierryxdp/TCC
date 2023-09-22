def media_matriz(x):
    for h in range(len(x)):
        soma=sum(x[h])/h
        for p in len(x[h]):
            media=soma/p
    return media