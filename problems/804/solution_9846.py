def filtra_pares(elementos):
    tupla_par=tuple()
    for numero in elementos:
        if numero%2==0:
			tupla_par=tupla_par+tuple(numero)
	return tupla_par