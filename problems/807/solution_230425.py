def conta_frases(s):
    ls=str.count(s,'...')+str.count(s,'!')+str.count(s,'?')
   	return str.replace(s,'...','XXX')