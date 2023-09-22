def conta_frases(s):
    '''Recebe um texto e retorna a quantidade de frases presentes nesse mesmo texto.'''
    '''String->int'''
    return str.count(s,'.')+str.count(s,'!')+str.count(s,'?')-2*str.count(s,'...')