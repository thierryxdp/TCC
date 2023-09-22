def eh_quadrada(mat):
    """Funcao que identifica se uma dada matriz e quadrada ou nao
entrada:
	mat -> list
saida: Bool"""
    
    print(len(mat))
	print(len(mat[0]))
    if len(mat) == len(mat[0]):
	    Return True
	else:
        Return False