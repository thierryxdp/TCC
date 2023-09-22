def media_matriz(m:list) -> float:
    acumulador=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            acumulador+=m[i][j]
    return round(acumulador/(len(m)*len(m[0])),2)