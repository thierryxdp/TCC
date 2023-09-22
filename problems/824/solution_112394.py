def uppCons(frase):
    '''Função que recebe uma frase e torna todas as suas
    consoantes em letras maiúsculas e mantém os demais caracteres
    no mesmo formato de entrada
    str -> str'''
    i = 0
    frase_atualizada = ''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            frase_atualizada = frase_atualizada + str.upper(frase[i])
		else:
            frase_atualizada = frase_atualizada + frase[i]
		i = i + 1            
	return frase_atualizada