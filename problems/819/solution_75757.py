def filtraMultiplos(lista,n):
    """Função que recebe como entrada uma lista de números e um número,
    e retorna outra lista contendo todos os elementos da lista original que
    forem divisíveis por n.
    lista, int -> lista
    """

	i = 0
	filtra = [ ]
	while i <len(lista):
		if lista[i] % n  == 0:
			filtra = filtra + [lista[i]]
		i = i+1
	return filtra