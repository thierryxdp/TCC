def conta_frase (texto):
    '''funçao que conta o numero de frases que aparecem no texto
    str-->int'''
    a=texto.count('!')
    b=texto.count('?')
    c=texto.count('.')
    d=texto.count9('...')
    soma=a+b+c+d
   	if ('.') and ('...') in texto:
    	return soma-3*a
    else:
        return soma