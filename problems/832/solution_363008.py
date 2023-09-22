def eh_quadrada(A):
    """"Reecebe uma matriz e retorna em booleanos se a matriz é quadrada ou não; list->bool."""
	if A==[]:
        return True
    
	linhas = len(A)
	colunas = len(A[0])
    
    if linhas!=colunas:
        return False
    
    else: 
        return True