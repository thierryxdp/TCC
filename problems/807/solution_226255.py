def conta_frases (frase):
    '''
    função que recebe um texto e retorna o numero de frases nele
    str -> int
    '''
    if str('...') in frase:
        return int(int(frase.count(str('.'))+frase.count(str('!'))+frase.count(str('?'))+frase.count(str('...'))) - 3)
    if 2*str('...') in frase:
        return int(int(frase.count(str('.'))+frase.count(str('!'))+frase.count(str('?'))+frase.count(str('...')))-6)
    else:
    	return int(frase.count(str('.'))+frase.count(str('!'))+frase.count(str('?')))