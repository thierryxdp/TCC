def faltante(lista):
    '''retorna a peça faltante de um quebra-cabeça
    list-> int'''
    i = 0

	if lista[0]!=1:
		return 1

	while i < len(lista):
		if (i+1) <= len(lista) and (lista[i]+1) != lista[i+1]:
			return i+2
        else:
            return len(lista)
		i += 1