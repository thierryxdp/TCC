def insere(lista_numero, n):
	"""Calcula e retorna a insercao do numero inteiro n
na lista "lista_numero",de modo que a mesma continue
sendo ordenada; list,int-->list"""
    a=list.append(lista_numero,n)
    b=list.sort(a)
    return b