def repetidos(listaN):
    '''retorna o número de vezes que um item da lista é maior que o anterior
    list -> int'''
    i=0
    counter=0
    while i < len(listaN):
    	if(listaN[i + 1] - listaN[i] > 0):
            counter += 1
            i += 1
    return counter