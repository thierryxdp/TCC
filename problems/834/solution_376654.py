def media_matriz(Matriz):
    elementos = 0
    soma = 0.0
    for i in len(Matriz[0]):
        for j in len(Matriz[0]):
            if i>=j and i<j:
                elementos += 1
                soma += Matriz[i][j]
    return round(soma/elementos,2)