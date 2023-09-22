def repetidos(numeros):
    """
    Função recebe como entrada uma lista de números, e retorna o número
    de vezes que um elemento da lista é igual ao elemento anterior.
    list -> int
    """
    i=1
    contador=0
    while i<len(numeros):
    	if numeros[i]==numeros[i-1]:
            i+=1
            contador+=1
        else:
            i+=1
	return contador