def repetidos(numeros):
    """
    	Função que retorna o número de vezes que um elemento
        da lista é igual ao elemento anterior.
    	list -> int
    """
    i = 0
    while i<len(numeros):
        repetidos = numeros.count(numeros[i])
        if i!= 0:
             repetidos>=numeros.count(numeros[i-1])
            return repetidos
        else:
            return numeros.count(numeros[i-1])
        i = i+1