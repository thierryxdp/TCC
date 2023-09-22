def uppCons(frase):
    '''retorna a frase dada com todas as suas consoantes em maiúsculas e os demais caracteres no formato original
    str -> str'''
	nova_frase = ''
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            nova_frase = nova_frase + frase[i].upper()
		else:
            nova_frase = nova_frase + frase[i]
		i = i + 1
	return nova_frase