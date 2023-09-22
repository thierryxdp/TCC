def repetidos(lista):
    """ Uma função que receba como entrada uma lista de números, e retorne o número
	de vezes que um elemento da lista  ́e igual ao elemento anterior
    list -> int"""

    
    i = 0
    ocorrencia = 0
    
    while i < len(lista):
        
        if (lista[i] == lista [i-1]):
            ocorrencia += 1
            
        i = i + 1
        
    return ocorrencia