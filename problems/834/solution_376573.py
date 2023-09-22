def media_matriz(Matriz):
    elementos = 0
    soma = 0.0
    for i in range(0,Matriz):
        for j in range(0,Matriz):
            if i>=j and i<j:
                elementos += 1
                soma += Matriz[i][j]
    return round(soma/elementos,2)