def media_matriz(matrix):
    lil_Li=0
    peso_pesado=len(matrix[0])*len(matrix)
    for j in matrix:
        for i in j:
        	lil_Li+=i
    return round(lil_Li/peso_pesado,1)