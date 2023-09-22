def uppCons(texto):
	"""transforma as consoantes minusculas de texto em maisculas
    str->str
    """
    lista_texto = list(texto)
	contador = 0
	letras = []
	while contador < len(lista_texto):
		if lista_texto[contador] in 'cbcdfghjklmnpqrstvwxyz':
			letras.insert(contador, lista_texto[contador].upper())
			contador = contador + 1
		else:
			letras.insert(contador, lista_texto[contador])
			contador = contador + 1
	return list.join(letras)