def media_matriz(matriz):
    '''retorna a média de todos os numeros da matriz
    [[]] -> float'''
    
    nCol = len(matriz)
    nLin = len(matriz[0])
    
    soma = 0
    
    for i in list(range(nCol)):
        for j in list(range(nLin)):
            soma = soma + matriz[i][j]
        
	t_num = nCol * nLin
    return round(soma / t_num, 2)