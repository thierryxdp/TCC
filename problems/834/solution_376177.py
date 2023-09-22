def media_matriz(lista):
    total = 0
    qntd = 0
    media = 0
    for linha in range(len(lista)):
        for coluna in range(len(lista[0])):
            total = total + lista[linha][coluna]
    qntd = linha*coluna
    media = total / qntd
    return round(2, media)