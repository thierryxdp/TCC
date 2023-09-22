def insere(lista_numero, n):
	"""Calcula e retorna a insercao do numero inteiro n
na lista "lista_numero",de modo que a mesma continue
sendo ordenada; list,int-->list"""
   	lista2= list.append(lista_numero,n)
	lista1 = list.sort (lista2)
    return lista1