def filtra_pares(a):
	'''Recebe uma tupla como quatro elementos inteiros como  e retorne uma nova tupla contendo apenas os elementos pares da tupla original
    tuple -> tuple'''
    if a[0]%2==0:
    	pares_novo=pares_novo+(a[0],)
    if a[1]%2==0:
    	pares_novo=pares_novo+(a[1],)
    if a[2]%2==0:
    	pares_novo=pares_novo+(a[2],)
    if a[3]%2==0:
    	pares_novo=pares_novo+(a[3],)
    return pares_novo