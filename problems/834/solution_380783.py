def media_matriz(matriz):
    soma=0
    d=0
    for i in range(len(matriz)):
        for x in matriz[i]:
            soma=soma+x
        	d=d+len(matriz[i])
    return round(d,2)