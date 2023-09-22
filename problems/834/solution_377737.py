def media_matriz(matriz):
    x=0
    z=0
    for i in matriz:
        z=z+len(i)
        for j in i:
            x=x+j
            
	return round (x/z)