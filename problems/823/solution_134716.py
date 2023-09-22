def faltante(lista):
    '''retorna a peça faltante de um quebra-cabeça
    list-> int'''
  	i = 0
	while i < len(lista)
		if (lista[i]+1) == lista[i+1]:
			return i+1
		i += 1