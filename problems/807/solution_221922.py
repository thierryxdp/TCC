def conta_frases(texto):
    '''Recebe uma string e retorna quantas frases ela têm; string->string'''
	conta_frases2=str.strip(conta_frases,'...')
    return str.count(conta_frases,'...')+str.count(conta_frases,'!')+str.count (conta_frases2,'.')+str.count(conta_frases,'?')