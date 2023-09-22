def filtra_pares(n):
	'''funcao que recebe uma tupla com 4 elementos e retorna uma
uma nova tupla contendo apenas os elementos pares da tupla original
	int -> int'''
    
	nv = ()
    
    if n[0] % 2 == 0:
        nv = nv + (n[0],)
	if n[1] % 2 == 0:
        nv = nv + (n[1],)
	if n[2] % 2 == 0:
        nv = nv + (n[2],)
	if n[3] % 2 == 0:
        nv = nv + (n[3],)
        
	return nv