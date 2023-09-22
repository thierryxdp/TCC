def filtra_pares(tup):
    '''fução que através de uma tupla de 4 elementos inteiros, filtra apenas os inteiros pares
e retorna os elementos pares na mesma ordem na qual foram inseridos
    int+int+int+int -> int'''

    pares = ()

    if tup [0]%2==0:
        pares = pares + (tup[0],)
    if tup [1]%2==0:
        pares = pares + (tup [1],)
    if tup [2]%2==0:
        pares = pares + (tup [2],)
	if tup [3]%2==0:
        pares = pares + (tup [3],)
        
        return pares