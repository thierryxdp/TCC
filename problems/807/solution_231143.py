def conta_frases(x):
    ponto = str.count(x,'.')
    exc = str.count(x,'!')
    retcs = str.count(x,'...')
    interrog = str.count(x,'?')
    if interrog = 0:
    	x = 0
	if retcs=0:
        x=0
    if exc = 0:
        x = 0
    if ponto=0:
        x=0
    else:
        x = ponto + exc + retcs + interrog
    return x