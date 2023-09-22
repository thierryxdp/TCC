def media_matriz(matriz):
    x=0
    z=0
    for i in matriz:
        for j in i:
            x=x+j
            z=z+len(j)
	return x/z