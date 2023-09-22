def insere(lista_numero, n):
	"""Calcula e retorna a insercao do numero inteiro n
na lista "lista_numero",de modo que a mesma continue
sendo ordenada; list,int-->list"""
    x = list.append(lista_numero,n)
   	x.sort()
    return x