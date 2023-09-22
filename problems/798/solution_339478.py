def freq_palavras(f):
    g = f.split()
    d={}
    for e in g:
        if e in d:
            d[e] = d[e] + 1
        else:
            d[e] = 1
	return d