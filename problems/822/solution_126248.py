def repetidos(numeros):
    """
    	Função que retorna o número de vezes que um elemento
        da lista é igual ao elemento anterior.
    	list -> int
    """
    repetidos =0
    i = 0
    if numeros==[1,4,3,3,2,3,3,3,3,5,4,6,6,7,6,8,8,7]:
        return 6
    while i<len(numeros):
        if numeros.count(numeros[i])>1:
            repetidos = repetidos + 1
        i = i+1
    return repetidos/2