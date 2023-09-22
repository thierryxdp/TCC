def filtra_pares(n):
	n = ()
	type(n) == tuple and len(n) == 4
	a = n[0]
	b= n[1]
	c = n[2]
	d = n[3]
	if a%2==0:
		n = n+(a,)
	if b%2==0:
		n = n+(b,)
	if c%2==0:
		n = n+(c,)
	if d%2==0:
		n = n+(d,)
		return n