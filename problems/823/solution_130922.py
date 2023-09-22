def faltante(lista):
    '''função que retorna o numero faltante numa sequencia '''
    '''list->int'''
    contador = 0
    indice = []
    while contador < len(lista):
        if lista[indice] == lista[indice + 1]:
            indice += 1
		else:
            contador = lista.append(lista[indice])
            indice += 1
	return contador