def conta_frases(texto):
    """conta o número de frases em um texto
    str->int"""
    if str.count(texto,'...')==1:
    	return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')+str.count(texto,'...')-3
    if str.count(texto,'...')==2:
        return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')+str.count(texto,'...')-6
    else:
        return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')+str.count(texto,'...')