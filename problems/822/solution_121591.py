def repetidos(lista):
    '''retorna o número de vezes que um elemento da lista é igual ao elemento anterior
    list->int'''
    ocorrencias=0
    i=0
    while i<len(lista)-1:
    	if lista[i]!=lista[i+1]:
    		i=i+1
    	if lista[i]==lista[i+1]:
            ocorrencias=ocorrencias+1
            i=i+1
    return ocorrencias