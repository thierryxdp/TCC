def repetidos(lista):
	'''função que recebe uma lista e retorna o número
    de vezes que um elemento da lista é igual o seu anterior
    list --> int'''
    i=0
    x=0
    while i<len(lista):
    	if lista[i]==lista[i-1]:
            x=x+1
        i=i+1
    return x