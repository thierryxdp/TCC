def repetidos(listanumeros):
    '''Retorna a quantidade de números iguais ao anterior na lista fornecida; lista ->int'''
    cont=0
    i=1
    while i <=len(listanumeros):
		if listanumeros[i] == listanumeros [i-1]:
        cont == (cont + 1)
    return cont