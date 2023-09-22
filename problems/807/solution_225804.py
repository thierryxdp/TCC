def conta_frases(frase):
    '''Esta e a funcao que conta o numero de frases que
    aparecem em um texto de entrada
    str -> int'''
    f1=frase.count('. ')
    f2=frase.count('!')
    f3=frase.count('?')
    f4=frase.count('...')
    f5=frase[-3:].count('.')
    f6=frase[-1].count('.')
    total1=f1+f2+f3+f4+f6
    total2=f1+f2+f3+f4
    if frase[-3:]!='...' and frase[-1]=='.':
	    return total1
	else:
        return total2