def repetidos(lista):
    '''	Dado uma lista de numeros, retorna o numero de vezes que um elemento da lista
    é igual ao elemento anterior.
    list -> int'''
	repetidos=0
    i=0
    while lista[i]<len(lista):
        if lista[i] in lista[:i]:
            repetidos=repetidos+1
    i=i+1
    return repetidos