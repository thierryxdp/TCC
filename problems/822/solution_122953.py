def repetidos(lista):
    """Dá o número de vezes que um elemento é igual ao elemento anterior
    	list -> int
        Parameters:
        lista: Lista de números
        
        Returns
        O número de vezes que um elemento da lista é igual ao anterior
    """
    
    cont = 0
    atual = 0
    anterior = 0
    vezes = 0
    
    while cont < len(lista):
        if contador == 0:
            atual = lista[cont]
        else:
            atual = lista[cont]
            if anterior == atual:
                vezes = vezes + 1
        anterior = atual
        cont = cont + 1
        
    return vezes