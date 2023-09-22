def lingua_p(palavra):
    '''Função que receba uma palavra e retorne a mesma palavra traduzida pra língua do P
    str -> str'''
    x = palavra.lower()
    y = ''
    vogais = 'aeiouàáâãéêíóúõô'
    for elem in x:
        y = y+elem
        if elem in vogais:
            y = y+ 'p' + elem
	return y