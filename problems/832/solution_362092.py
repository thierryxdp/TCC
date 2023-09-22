def eh_quadrada(matriz):
    """retorna True caso a matriz de entrada seja quadrada, caso não seja, retorna o valor booleano False,
    	(list) -> bool"""
    linha = 0
    coluna = 0
    for i in matriz:
        linha = linha + 1
        for j in matriz[i][j]:
            coluna = coluna + 1
	if linha == coluna:
        return True
    else:
        return False