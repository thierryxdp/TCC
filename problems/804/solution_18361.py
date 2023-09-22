def filtra_pares(tupla):
	"""A função recebe como entrada uma tupla com quatro elementos
	inteiros e retorna outra tupla contendo apenas os elementos
	pares da tupla inicial, na mesma ordem em que se encontravam."""
	tupla_final = ()
    if (tupla[0])%2 == 0:
        tupla_final = tupla_final + (tupla[0],)
    if (tupla[1])%2 == 0:
        tupla_final = tupla_final + (tupla[1],)
    if (tupla[2])%2 == 0:
        tupla_final = tupla_final + (tupla[2],)
    if (tupla[3])%2 == 0:
        tupla_final = tupla_final + (tupla[3],)
        
    return tupla_final