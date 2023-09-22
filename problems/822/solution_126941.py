def repetidos(lista:list)->int:
    '''retorna quantas vezes um número é igual ao anterior'''
    i=1
    contador = 0
    while i <= len(lista):
        if lista[i] == lista[i-1]:
            contador += 1
		i += 1
	return contador