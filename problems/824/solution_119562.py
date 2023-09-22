def uppCons(frase):
	""" Dado uma frase retorna todas as consoantes da frase com letras maiúculas.
        entrada string -> saida string. """
	
	i = 0
    fraseFinal = ''
	while i < len(frase):
		if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            fraseFinal = fraseFinal + str.upper(frase[i])
        else:
            fraseFinal = fraseFinal + frase[i]
		i = i + 1
	return fraseFinal