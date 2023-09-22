def intercala(lista1,lista2):
	"""intercala duas listas, comecancando pela lista1.entra lista1 e lista2;
list,list->list"""
	lista3=lista1[:1]+lista2[:1]+lista1[1:2]+lista2[1:2]+lista1[2:]+lista2[2:]
	return lista3