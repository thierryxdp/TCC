def repetidos(lista):
    '''Recebe como entrada uma lista de números(list), e retorne o número de vezes que um elemento da lista é igual
    ao elemento anterior(int).'''
    x=1
    contador=0
    while x < len(lista):
        if lista[x] == lista[x-1]:
            contador=contador+1
        x=x+1
	return contador