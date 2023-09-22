def conta_frases(x):
    if '.' or '!' or '?' or '...' in x:
		y1 = x.count('.')
        y2 = y1.count('!')
        return y