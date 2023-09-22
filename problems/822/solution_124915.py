def repetidos(lista):
    '''Função que recebe uma lista de números e verifica quantas
    vezes um elemento da lista é igual ao anterior
    lista -> int'''
    indice = 1
    contador = 0
    while indice < len(lista):
        if lista[indice] == lista[indice - 1]:
			contador += 1
		indice += 1
	return contador