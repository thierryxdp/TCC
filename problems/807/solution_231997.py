def conta_frases(x):
    if '.' or '!' or '?' or '...' in x:
		y1 = x.count(' .')
        y2 = x.count('!')
        y3 = x.count('?')
        y4 = x.count('...')
        return y1 + y2 + y3 + y4