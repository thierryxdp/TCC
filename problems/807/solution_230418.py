def conta_frases(s):
    ls=str.count(s,'!')+str.count(s,'?')+str.count(s,'...')
    if('.' not in s):
    	return ls
    if('...'in s) and ('.' in s):
        str.count(s,'.')-3
    return str.count(s,'.')+ls