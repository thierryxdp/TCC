def repetidos(listanum):
    '''funcao que dada uma lista de numeros, retorna o numero de vezes que um elemento da lista eh igual ao elemento anterior
    list -> int '''
    i = 1
    j = 0
    contador = 0
    while(i < len(listanum)):
    	if(listanum[i] == listanum[j]):
        	contador += 1
        	i += 1
        	j += 1
        else:
        	i += 1
        	j += 1
    return contador