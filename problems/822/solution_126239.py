def repetidos(numeros):
    """
    	Função que retorna o número de vezes que um elemento
        da lista é igual ao elemento anterior.
    	list -> int
    """
    i = 0
    while i<len(numeros):
        repetidos = numeros.count(numeros[i])
        if repetidos<numeros.count(numeros[i-1]):
            repetidos = numeros.count(numeros[i-1])
        elif repetidos>=numeros.count(numeros[i-1]):
            repetidos = repetidos
        i = i+1
    return repetidos