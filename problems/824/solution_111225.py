def uppCons(frase):
    '''A partir da frase do parametro torna todas as consoantes
    maiusculas(vogais e simbolos nao sao afetados
    str -> str'''
    consoantes = 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZçÇ'
    k = 0
    while k < len(frase):
        if frase[k] in consoantes:
            frase = str.replace(frase,frase[k],str.upper(frase[k]),1)
        k += 1
	return frase