def conta_frases(texto):
    if texto[-1]=='.':
    	return str.count(texto,'. ')+str.count(texto,'?')+str.count(texto,'!')+1
    else:
        return str.count(texto,'. ')+str.count(texto,'?')+str.count(texto,'!')