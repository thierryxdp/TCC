def filtraMultiplos(lista,n):
    '''Dada como entrada uma lista e um numero, todos inteiros,
    retorna uma outra lista contendo os numeros divisiveis por n
    list, int -> list'''
    lista_nova = []
    contador = 0
    while contador < len(lista):
		if lista[contador] % n == 0:
        	lista_nova.append(lista[contador])
		contador +=1
	return lista_nova