def repetidos(lista):
    """Função que recebe uma lista de numeros e retorna o numero de vezes que um
    elemento da lista é igual ao anterior.
    list -> int."""
    soma = 0
    indice = 1
    while indice < len(lista):
        if lista[indice] == lista[indice-1]:
            soma += 1
		indice += 1
	return soma