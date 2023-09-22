def media_matriz(matriz):
    i=0
    soma=[]
    while i<len(matriz):
        soma=soma+[sum(matriz[i])]
        i=i+1
    return sum(soma)/(len(matriz)*len(matriz[i])