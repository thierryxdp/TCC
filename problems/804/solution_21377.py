def filtra_pares(a,b,c,d):
	'''função que, dado uma tupla de 4 elementos, retorna somente os números pares
       tuple -> tuple'''
    pares=()
    if a%2==0:
    	pares+(a,)
    if b%2==0:
        pares+(b,)
    if c%2==0:
        pares+(c,)
    if d%2==0:
        pares+(d)
     return pares