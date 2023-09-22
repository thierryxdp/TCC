def lingua_p(palavra):
    '''Função que recebe uma palavra e retorna a mesma palavra traduzida para lingua do P.'''
    '''str -> str'''
	palavra_traduzida= ''
	for letra in str.lower(palavra):
		if letra in 'aeiouúãáâéôõó':
			palavra_traduzida += letra + 'p' + letra
		if letra in 'bcdfghjklmnpqrstvwxyz':
			palavra_traduzida += letra
	return palavra_traduzida