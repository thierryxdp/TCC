def repetidos(lista):
    """Retorna a quantidade de vezes que um numero é igual a seu anterior da lista;
    list -> int"""
    numero_anterior = lista[0]
    cont = 1
    vez = 0
    while cont < (len(lista) - 1):
        if lista[cont] == numero_anterior:
            vez += 1
        numero_anterior = lista[cont]
	return vez