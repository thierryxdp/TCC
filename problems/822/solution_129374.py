def repetidos(lista):
    """ função que recbe uma lista como entrada e retorna o número
    	de vezes que um elemento da lista e igual ao elemento anterior. lista --> int"""
    
    elementoAnterior = ""
    cont = 0
    for elemento in lista:
        if elemento == elementoAnterior:
            cont += 1
        elementoAnterior = elemento 
    return count