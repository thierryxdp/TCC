def exclamacao (frase):
    '''retorna quantidade de frases com exclamação
    str -> int'''
    return str.count (frase,'!')

def interrogacao (frase):
    '''retorna quantidade de frases com interrogação
    str->int'''
    return str.count (frase,'?')

def reticencia (frase):
    '''retorna quantidade de frases com reticência
    str->int'''
    return str.count (frase,'...')

def ponto (frase):
    '''retorna quantidade de frases com ponto
    str->int'''
    return str.count (frase,'.') - 3*str.count (frase,'...')

def conta_frases (frase):
    '''retorna a quantidade de frases que tem na frase
    str->int'''
    return ponto (frase)+ reticencia (frase)+ interrogacao (frase)+ exclamacao (frase)