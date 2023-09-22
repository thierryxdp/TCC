def repetidos(lista):
    """Função que recebe uma lista de números e retorna a
quantidade de vezes que um elemento da lista é igual ao
anterior.
	list -> int"""

    i = 0
    n_repeticoes = 0
    
    while i < len(lista) - 1:
        if lista[i] == lista[i+1]:
            n_repeticoes += 1
		i +=1    
    
    return n_repeticoes