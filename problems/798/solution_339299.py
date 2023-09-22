def freq_palavras(f):
	d={}
	for r in f:
		if p(r) in d:
			d[p(r)] = 1 + d[p(r)]
		else:
			d[p(r)] = 1
	return f[0]
def p(r):
    return r[0]