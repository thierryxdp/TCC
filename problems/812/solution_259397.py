def eh_ordenada(lista):
	'''
	Retorna uma tupla dizendo se a lista está ordenada e se está ordenada em ordem crescente ou decrescente
	'''
	ordenada = 0

	if lista == sorted(lista, reverse=False): ordenada = 1
	if lista == sorted(lista, reverse=True): ordenada = -1

	status = "crescente" if ordenada == 1 else ("decrescente" if ordenada == -1 else "desordenada")

	tupla = (bool(ordenada), status)

	return tupla