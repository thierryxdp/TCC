def media_matriz(matriz:list[list])->float:
    soma = 0
    total = 0
    for i in matriz:
        soma += sum(i)
        total += len(i)
    return round(soma/total, 2)