def freq_palavras(frases):
    d = {}
    j = []
    for i in frases.split(' '):
        if i not in j:
        	d[i] = frases.count(i)
		j.append(i)
    return d