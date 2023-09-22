def repetidos (lista):
    '''função que retorna o numero de vezes que um elemento da lista é igual ao elemento anterior;
    list->int'''
    i = 0
	n = 0  
	while i<len(lista):
        if lista[i+1] == lista[i]:
            n = n+1
        else:
            n = n + 0
        i = i+1
    return n