def repetidos(lista):
    """
    Recebe uma lista de numeros e retorna o numero de vezes
    que um elemento da lista é igual ao elemento anterior;
    list -> list
    """
	pos = []    
    i = 0
    
    while i <= len(lista):
        pos = lista.count(i)
        i=i+1
        
    return pos