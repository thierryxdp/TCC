def repetidos(lista):
    """Funcao que recebe como entrada uma lista de numeros e retorna o numero
    	de vezes sque um elemento da lista e igual ao elemento anterior"""
    n = 1
    contador = 0
	while n<len(lista):
        if lista[n]==lista[(n-1)]:
            contador = contador + 1
        n +=1
    return contador