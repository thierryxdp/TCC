def faltante (L):
    contador = 1
    while contador < len (L):
        if contador not in L:
            return contador
        contador += 1
	return L[contador] - 1