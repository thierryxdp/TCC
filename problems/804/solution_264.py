def filtra_pares(tupla):
	el1, el2, el3, el4 = tupla
    resultado = ()
	if not (el1%2):
		resultado += el1
	if not (el2%2):
		resultado += el2
	if not (el3%2):
		resultado += el3
	if not (el4%2):
		resultado += el4
	return resultado