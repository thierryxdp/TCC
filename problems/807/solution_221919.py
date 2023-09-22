def conta_frases(texto):
    '''Recebe uma string e retorna quantas frases ela têm; string->string'''
	a=str.count(conta_frases,'...')
    conta_frases2=str.strip(conta_frases,'...')
    b=str.count(conta_frases,'!')
    c=str.count (conta_frases2,'.')
    d=str.count(conta_frases,'?')
    return a+b+c+d