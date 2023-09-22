def maiores(lista_numint,n)
	'''
    funcao que recebe uma lista com numeros inteiros 
    e um numero inteiro n e retorna outra lista com os 
    numeros inteiros maiores do que n em ordem crescente
    
    list, int -> list
    '''

	a = ([i for i in lista_numint if i  n])
	return sorted (a)