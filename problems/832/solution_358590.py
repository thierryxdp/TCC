def eh_quadrada(mat):
    """Funcao que identifica se uma dada matriz e quadrada ou nao
entrada:
	mat -> list
saida: Bool"""
    
    
    if mat == []  or len(mat) == len(mat[0]):
        return True
	else:
        return False