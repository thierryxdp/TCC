def filtra_pares(tupla):
	"""A função recebe como entrada uma tupla com quatro elementos
	inteiros e retorna outra tupla contendo apenas os elementos
	pares da tupla inicial, na mesma ordem em que se encontravam."""
	nova_tupla = ()
    if tupla[0]%2 == 0:
        nova_tupla = nova_tupla + (tupla[0])
    elif tupla[1]%2 == 0:
        nova_tupla = nova_tupla + (tupla[1])
    elif tupla[2]%2 == 0:
        nova_tupla = nova_tupla + (tupla[2])
    elif tupla[3]%2 == 0:
        nova_tupla = nova_tupla + (tupla[3])
        return nova_tupla