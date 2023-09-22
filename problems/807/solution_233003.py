def conta_frases(texto):
	l1 = texto.split('.')
    l2 = texto.plit('!')
    l3 = texto.split('...')
    l4 = texto.split('?')
    return len(l1) + len(l2) + len(l3) + len(l4)