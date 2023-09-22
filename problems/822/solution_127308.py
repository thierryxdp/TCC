def repetidos(lista):
    '''Recebe como entrada uma lista de números
    e retorna o número de vezes que um elemento
    da lista é igual ao elemento anterior.
    list -> int'''
    x = 0
    repetido = 0
    while x < len(lista):
        if lista[x] in lista:
            repetido += lista[x]
    	return repetido
            
        x += 1