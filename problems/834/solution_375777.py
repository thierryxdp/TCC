def media_matriz(Matriz):
    elementos = 0
    soma = 0.00
    for i in range(0,10):
        for j in range(0,10):
            if i>=j:
                elementos += 1
                soma += Matriz[i][j]
    return soma/elementos