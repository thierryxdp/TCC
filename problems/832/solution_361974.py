def eh_quadrada(M):
	'''Retorna True se a matriz M de entrada for quadrada;
    False, caso contrário;
    list[list[int]] -> bool'''
    linhas=len(M)
    colunas=len(M[0])
    if linhas==colunas:
        return True
    else:	
        return False