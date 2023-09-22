def filtra_pares(tupla):
	a,b,c,d = tupla
	resultado = ()
	if a%2==0:
		resultado = resultado + (a,)
	if b%2==0:
		resultado = resultado + (b,)
	if c%2==0:
		resultado = resultado + (c,)
	if d%2==0:
		resultado = resultado + (d,)
	return resultado