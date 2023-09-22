def filtra_pares(n):
	type(n) == tuple and len(n) == 4
	a = ()
	if n[0]%2==0:
		a = a+(n[0],)
        else:
            a= a+(,)
	if n[1]%2==0:
		a = a+(n[1],)
	if n[2]%2==0:
		a = a+(n[2],)
	if n[3]%2==0:
		a = a+(n[3],)
	return a