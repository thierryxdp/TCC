def uppCons(frase):
'''Dado uma frase modifica todos as consoantes minisculas para maisculas.
str->str'''
	i = 0
	frase2 = []
	while i < len(frase):
		if str.lower(frase[i]) in "bcdfghjklmnpqrstvxywzç":
			list.append(frase2, str.upper(frase[i]))
		else:
			list.append(frase2, frase[i])
		i = i + 1
	return str.join("", frase2)