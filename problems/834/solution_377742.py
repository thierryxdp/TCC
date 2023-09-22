def media_matriz(matriz):
    '''retorna a media de todos os numeros da matriz
    entrada:list
    saida:float'''
    x=0
    z=0
    for i in matriz:
        z=z+len(i)
        for j in i:
            x=x+j
           
	return round (x/z, 2)