def eh_quadrada(mat):
    """Funcao que identifica se uma dada matriz e quadrada ou nao
entrada:
	mat -> list
saida: Bool"""
    
    
    if len(mat) == len(mat[0]) or mat == [] :
        return True
	else:
        return False