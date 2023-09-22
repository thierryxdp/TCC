def conta_frases (frase):
    '''
    função que recebe um texto e retorna o numero de frases nele
    str -> int
    '''
    if str('...') in frase:
        return int(frase.count('. ')+frase.count(str('!'))+frase.count(str('?'))+frase.count(str('...'))+frase.count(str('... ')))
    if str('... ') in frase and len(str('...') > 1:
        return int(int(frase.count('.')+frase.count(str('!'))+frase.count(str('?'))+frase.count(str('...'))+frase.count(str('... ')))-3)
    else:
    	return int(frase.count(str('.'))+frase.count(str('!'))+frase.count(str('?')))