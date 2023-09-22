def conta_frases (texto):
    '''retorna a quantidade de frases que aparecem no texto;string -> int'''
    return texto.count('!') + texto.count('.') + texto.count('?') - 2*texto.count('...')