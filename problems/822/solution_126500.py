def repetidos(lista):
    """função que gera o número de vezes que o elemento da lista
    é semelhante ao elemento anterior
    list -> int"""
	numVezes = 0
    contador = 0
    while contador < len(lista):
        if (lista[contador]) == (lista[contador -1]):
            numVezes += 1
        contador += 1
    return