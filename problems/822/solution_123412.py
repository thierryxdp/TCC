def repetidos(lista):
    """Dá o número de vezes que um elemento é igual ao elemento anterior"""
    
    cont = 0
    atual = 0
    anterior = 0
    vezes = 0
    
	for i in range len(lista):
        if i == 0:
            atual = lista[i]
        else:
			atual = lista[i]
            if anterior == atual:
                vezes = vezes + 1
        anterior = atual
    i =+ 1
        
    return vezes