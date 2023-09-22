def media_matriz(matriz):
    i=0
    soma=[]
    while i<len(matriz):
        i=i+1
        soma=soma+sum(matriz[i])
    return sum(soma)