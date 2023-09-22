def filtra_pares(t):
	'''função que recebe uma tupla com 4 elementos e retorna somente os pares na mesma ordem'''
	'''tupla -> tupla ''' 
    n=()
    if t[0] % 2 == 0:
        n = n + (t[0],)
    if t[1] % 2 == 0:
        n = n + (t[1],)
    if t[2] % 2 == 0:
        n = n + (t[2],)
    if t[3] % 2 == 0:
        n = n + (t[3],)
    
    return n