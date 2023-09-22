def conta_frases(x):
	return x[0] + x.count('.') + x.count(':') + x.count(';') + x.count('!') + x.count('?')