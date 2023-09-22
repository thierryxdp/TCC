def conta_frases(texto):
	l1 = texto.split('. ', texto.count('. ') - 1)
    l2 = texto.split('! ')
    l3 = texto.split('...')
    l4 = texto.split('? ')
    return l1