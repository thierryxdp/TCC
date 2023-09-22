def uppCons(frase):
	""" Dado uma frase retorna todas as consoantes da frase com letras maiúculas.
        entrada string -> saida string. """
	
	i = 0
	while i < len(frase):
		if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            str.upper(frase)
		i = i + 1
	return frase