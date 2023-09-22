def conta_frases(x):
	if '...' in x:
		y1 = x.count('.')
        y2 = x.count('!')
        y3 = x.count('?')
        y4 = x.count('...')
        ye = len(y4) * 3
        return y1 + y2 + y3 + y4 - ye
    if '...' not in x:
        y1 = x.count('.')
        y2 = x.count('!')
        y3 = x.count('?')
        return y1 + y2 + y3