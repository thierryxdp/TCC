def media_matriz(m):
    elementos = []
    soma = 0
    
    for i in range(len(m)):
        for j in range (len(m[0])):
            elementos = elementos + [m[i][j]]
    soma = sum(elementos)
    media = soma/len(elementos)
    
    return media