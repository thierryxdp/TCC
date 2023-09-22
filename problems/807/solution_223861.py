def conta_frases(n):
	A = str.replace(n,'...','.')
    A = str.replace(n,'!','.')
    A = str.replace(n,'?','.')
    return str.count(A,'.')