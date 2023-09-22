def media_matriz(m):
    numeros = []
    soma = 0
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            numeros = numeros + [m[i][j]]
            
    soma = sum(numeros)
    media = soma/len(numeros)
    
    return round(media,2)