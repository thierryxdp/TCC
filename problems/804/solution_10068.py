def filtra_pares(elementos):
    tupla_par=tuple()
    x=0
    for numero in elementos:
        if numero%2==0:
			tupla_par+=tuple(elementos[x])
		x+=1
    return tupla_par