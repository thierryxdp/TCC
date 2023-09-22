def filtra_pares(a,b,c,d):
    tupla_par=tuple()
    for numero in (a,b,c,d):
        if numero%2==0:
            tupla_par+=numero
	return tupla_par