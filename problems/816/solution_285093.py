def maiores(lista,n):
    '''cria uma lista com os números maiores que "n"presentes numa lista'''
    # se não está na lista, inclua
    if n not in lista:
		lista.insert(0, n)
	
    # ordena
    lista.sort()
    
    # encontra a posicao
	indice = lista.index(n)
    
    # retorna somente os maiores
    return lista[indice+1:]