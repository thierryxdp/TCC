def conta_frases(x):
    x.replace('...','.')
    
    if x.count(".")>0 or x.count("!")>0 or x.count("?")>0:
    	k =x.count(x.replace('...','.'))
    	l =x.count("!")
    	m =x.count("?")
    return k + l + m