def filtra_pares (t):
    pares=tuple()
    
	if t[0]%2==0:
        pares=+(t[0],)
	if t[1]%2==0:
        pares=+(t[1],)
	if t[2]%2==0:
        pares=+(t[2],)
	if t[3]%2==0:
        pares=+(t[3],)
	
        return pares