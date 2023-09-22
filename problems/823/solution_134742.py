def faltante(lista):
    '''retorna a peça faltante de um quebra-cabeça
    list-> int'''
    i = 0

	if lista[0]!=1:
		return 1

	if lista[len(lista)-1]!=len(lista):
		return len(lista)

	while i<len(lista):
		if (lista[i]+1) != lista[i+1]:
			return i+2
		i += 1