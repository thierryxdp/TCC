def lingua_p(palavra):
	palavra_traduzida= ''
	for letra in str.lower(palavra):
		if letra in 'aeiouúãáâéôõó':
			palavra_traduzida += letra + 'p'
		if letra in 'bcdfghjklmnpqrstvwxyz':
			palavra_traduzida += letra
	return palavra_traduzida