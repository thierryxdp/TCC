def eh_quadrada (matriz):
    """Funcao retorna True caso a matriz seja quadrada ou False caso contrario
    list -> bool"""
  	linha = len(matriz)
    if linha == 1:
        return True
    else:
        a = matriz[0]
    	if len(a) == linha:
       		return True
    	else:
        	return False