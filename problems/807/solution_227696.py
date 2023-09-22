def conta_frases(texto):
    '''
    Recebe um string texto e retorna o número de frases no texto
    
    str -> int
    '''    
    if texto[-1]=='.':
    	return str.count(texto,'. ')+str.count(texto,'?')+str.count(texto,'!')+1
    else:
        return str.count(texto,'. ')+str.count(texto,'?')+str.count(texto,'!')