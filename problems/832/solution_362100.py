def eh_quadrada(matriz):
    """retorna o valor booleano True se a matriz de entrada for quadrada, caso não seja, retorna o valor booleano False,
    	(list) -> bool"""
    linha = 0
    coluna = 0
    for i in range(len(matriz)+1):
        linha = linha + 1
    for j in range(len(matriz[i]+1)):
        coluna = coluna + 1
    if linha==coluna:
        return True
    else:
        return False