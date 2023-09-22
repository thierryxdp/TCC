def media_matriz(Matriz):
    elementos = 0
    soma = 0.0
    for i in len(Matriz):
        for j in len(Matriz[0]):
            if i>=j and i<j:
                elementos += 1
    soma += len(Matriz)*len(Matriz[0])
    return round(soma/elementos,2)