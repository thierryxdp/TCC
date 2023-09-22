def conta_frases(s):
    ls=str.count(s,'!')+str.count(s,'?')+str.count(s,'...')+str.count(s,'.')
    if('.' not in s):
    	return ls
    return str.count(s,'.')