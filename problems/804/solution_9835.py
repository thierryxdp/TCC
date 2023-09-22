def filtra_pares(a,b,c,d):
	tupla_inteira=(a,b,c,d)
    tupla_par=tuple()
    for numero in tupla_inteira:
        if numero%2==0:
            tupla_par+=numero
    return tupla_par