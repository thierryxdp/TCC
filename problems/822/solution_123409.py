def repetidos(lista):
    """Dá o número de vezes que um elemento é igual ao elemento anterior"""
    
    cont = 0
    atual = 0
    anterior = 0
    vezes = 0
    
    for i in range len(lista):
        if cont == 0:
            atual = lista[cont]
        else:
			atual = lista[cont]
            if anterior == atual:
                vezes = vezes + 1
        anterior = atual
        i =+ 1
        
    return vezes