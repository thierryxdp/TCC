def repetidos(lista):
    '''Dada como entrada uma lista de numeros, retorna o 
    numero de vezes que um elemento da lista é igual ao 
    elemento anterior
    list -> int'''
    contador = 0
    elementos = 0
    while contador<len(lista):
        if lista[contador] == lista[contador-1]:
			elementos += 1
		contador +=1
	return elementos