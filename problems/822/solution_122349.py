def repetidos(lista):
    """essa funcao, dada uma lista de numeros,
	 retorna o numero de vezes que um elemento da lista eh igual ao anterior
     list -> int"""
    i = 0
    lista_dois = []

    while i < len(lista):
        if lista[i] == lista[i-1]:
            lista_dois = lista_dois + [lista[i], ]
        i = i + 1
    return len(lista_dois)