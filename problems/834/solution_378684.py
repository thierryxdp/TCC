def media_matriz(x):
    for h in range(len(x)):
        for p in len(x[h]):
            soma=sum(x[h])/h
            media=soma/p
    return media