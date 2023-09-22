def conta_numero(numero,matriz):
    """
    	Retorna quantas vezes um número aparece na matriz.
        int, lista -> int
    """
    vezes= 0
    for i in range(len(matriz)):
        if i == numero:
            vezes += 1
	return vezes