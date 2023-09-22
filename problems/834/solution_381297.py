def media_matriz(m):
    soma=0
    i=0
    j=0
    while i<len(m):
        while j<len(m[0]):
            soma = soma+m[i][j]
            j=j+1
        i=i+1
        j=0
    return soma