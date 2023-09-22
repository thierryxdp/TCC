def media_matriz(m):
    total = 0
    contagem = 0
    for i in m:
        total = total + sum(i)
        contagem = contagem + len(i)
    return round(total/contagem,2)