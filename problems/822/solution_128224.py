def repetidos (lista):
    """ Dados uma lista de inteiros, retorna o número de vezes que um elemento é igua ao anterior.
    entrada lista -> saida int."""
    
    anterior = 0
    qtd_repeticoes = 0 
    
    i = 1
    while i < len(lista):
        anterior = lista[i-1]
        if lista[i] == anterior:
            qtd_repeticoes = qtd_repeticoes + 1
        i = i + 1
	return qtd_repeticoes