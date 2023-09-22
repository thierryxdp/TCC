def lingua_p(palavra):
	’’’fun ̧c~ao que recebe palavra em portugu^es e
	retorna palavra traduzida em lingua do p.
	str--> str’’’
	traduzido_p = []
	contador = 0
	for letra in list(palavra):
		if letra in ’aeiou a e i o u’:
			traduzido_p.append(letra + ’p’ + letra)
		else:
			traduzido_p.append(letra)
	return ’’.join(traduzido_p)