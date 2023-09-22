def freq_palavras(f):
	d={}
	for r in rs:
		if p(r) in d:
			d[p(r)] = 1 + d[p(r)]
		else:
			d[p(r)] = 1
	return d
def p(r):
    return r[0]