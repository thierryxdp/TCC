def eh_quadrada(matriz):
    """retorna o valor booleano True caso a matriz de entrada seja quadrada, caso a matriz não seja quadrada, retorna o valor booleano False
    	(list) -> bool"""
    linhas = 0
    colunas = 0
    for i in range(len(matriz)):
        linhas = linhas + 1
        for j in range(len(matriz[i][j])):
            colunas = colunas + 1
  	if colunas == linhas:
        return True
    else:
        return False