def eh_quadrada(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha!=0 and coluna!=0:
        return False
    if linha==0 and coluna!=0:
        return False
    if linha!=0 and coluna==0:
    	return False
    else:
        return True