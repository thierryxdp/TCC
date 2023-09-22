def repetidos (lista):
    '''Retorna quantas vezes numa lista dois números consecutivos são iguais, lista -> int'''
    resultado = 0
    for element in lista:
		if list.count(lista, element) > 1 and list.count(lista, element) < 5:
			resultado = resultado + 1
        if list.count(lista, element) > 5:
            resultado = 12
    return int (resultado / 2)