def uppCons(frase):
	return [char if char in ['a', 'e', 'i', 'o', 'u'] else char.upper() for char in frase]