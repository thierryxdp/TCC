def eh_quadrada(A):
    """"Reecebe uma matriz e retorna em booleanos se a matriz é quadrada ou não; list->bool."""
	linhas = len(A)
	colunas = len(A[0])
    
    if linhas!=colunas:
        return False
    
    else: 
        return True