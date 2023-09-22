def insere(lista_numero, n):
	"""Calcula e retorna a insercao do numero inteiro n
na lista "lista_numero",de modo que a mesma continue
sendo ordenada; list,int-->list"""
    lista_numero = list.append(lista_numero,n)
    return list.sort(lista_numero)