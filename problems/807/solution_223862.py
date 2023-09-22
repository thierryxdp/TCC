def conta_frases(n):
	A = str.replace(n,'...','.')
    A = str.replace(A,'!','.')
    A = str.replace(A,'?','.')
    return str.count(A,'.')