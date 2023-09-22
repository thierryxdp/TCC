def filtraMultiplos(lista, n):
    """Função que recebe uma lista de numeros e um numero e retorna outra lista contendo
    todos os elementos da lista original que forem divisiveis por n.
    list, int -> list."""
    listaFinal = []
    contador = 0
    while contador < len(lista):
        if lista[contador] % n == 0:
            listaFinal = listaFinal + [lista[contador]]
		contador = contador + 1
	return listaFinal