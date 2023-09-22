def filtra_pares (tuple):
        
    pares = ()
    
    if tuple [0] % 2 == 0:
        pares = pares + (tuple [0], )
    if tuple [1] % 2 == 0:
        pares = pares + (tuple [1], )
    if tuple [2] % 2 == 0:
        pares = pares + (tuple [2], )
    if tuple [3] % 2 == 0:
        pares = pares + (tuple [3], )
        
	return pares