def repetidos(lista):
    '''Dada uma lista, a função retorna o número de vezes que um elemento
       da lista é igual ao anterior.
       list -> int
       Parametros:
       lista: lista a ser digitada'''
    i = i2= ni = n2 = 0
    while i < len(lista):
        n1 = lista[i]
        n2 = lista[i + 1]
        if n1 == n2:
            i2 += 1
            i += 1
    	i += 1
            
	return i2