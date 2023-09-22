def uppCons(frase):
	""" esta função retorna todas as consoantes maiusculas
	str -> str """
	i = 0 
	maiuscula = ''
	f_maiuscula = ''
	while i < len(frase):
		maiuscula = frase [i]
		if frase[i] in 'bcçdfghjklmnpqrstvxywz':
			maiuscula = str.upper(maiuscula)
		f_maiuscula = f_maiuscula + maiuscula
		i = i + 1
	return f_maiuscula