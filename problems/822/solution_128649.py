def repetidos (lista):
    '''Retorna quantas vezes numa lista dois números consecutivos são iguais, lista -> int'''
    resultado = 0
    for element in lista:
        list.count(element)
		if list.count(element) > 1:
			resultado = resultado + 1
    return resultado