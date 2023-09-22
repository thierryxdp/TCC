def repetidos (lista):
    '''Retorna quantas vezes numa lista dois números consecutivos são iguais, lista -> int'''
    resultado = 0
    for element in lista:
        list.count(lista, element)
		if list.count(lista, element) > 1:
			resultado = resultado + 1
    return resultado / 2