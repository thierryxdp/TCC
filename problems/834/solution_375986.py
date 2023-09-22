def media_matriz(matriz):
    T=0
    for l in range(len(matriz)):
        for i in range(len(matriz[0])):
   		 	T=T+sum(matriz[i])
        return T