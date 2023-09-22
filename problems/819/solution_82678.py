def filtra_multi(l, n):
	'''esta função mostra os multiplos de um deteminado número (n)
	de acordo com a lista de números fornecidos'''
	multi = []
	proximo = 0
	while proximo <len(l):
		if l[proximo]%n == 0:
			multi = multi + [l[proximo],]
		proximo = proximo + 1
	return multi