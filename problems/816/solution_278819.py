def maiores(lista, numero):
    '''Essa função irá retornar uma lista com os elementos maiores que os elementos passados 
    dentro da variável n
    Entrada: Lista | Saída: Lista
    '''
	lista.append(numero)
	if max(lista) == numero:
		return []
	else:
        lista_decrescente = sorted(lista, reverse = True)
        index_n = lista_decrescente.index(numero)
        return sorted(lista_decrescente[:index_n])