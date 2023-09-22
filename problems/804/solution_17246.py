def filtra_pares(n):
	type(n) == tuple and len(n) == 4
	if n[0]%2==0:
		n = n+(n[0],)
	if n[1]%2==0:
		n = n+(n[1],)
	if n[2]%2==0:
		n = n+(n[2],)
	if n[3]%2==0:
		n = n+(n[3],)
		return n