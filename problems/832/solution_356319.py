def eh_quadrada(matriz):
    if matriz==[[[]]]:
        return True
    linha = len(matriz)
    coluna = len(matriz[0])
    if matriz==[[[]]]:
        return True
    if linha==coluna:
        return True
    if linha!=0 and coluna!=0:
        return False
    if linha==0 and coluna!=0:
        return False
    if linha!=0 and coluna==0:
    	return False
    else:
        return True