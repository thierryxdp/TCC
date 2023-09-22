def eh_quadrada(matriz):
    """ Função que identifica se uma matriz é quadrada; list-> bool"""
    matriz_r=list()
    nlinhas= len(matriz)
    ncolunas= len(matriz[])
	for i in range(nlinhas):
    	list.append(matriz_r,[0]*ncolunas)
        for j in range(ncolunas):
            matriz_r[i][j]=matriz[i][j]
    if matriz_r== [i] and [j]:
        return True
    else:
        return False