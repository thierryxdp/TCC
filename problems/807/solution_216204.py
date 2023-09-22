def conta_frases(texto):
    '''Conta o número de frases presentes no texto recebido
    string-> int'''
    text= texto.replace('...','.')
    n1 = text.count('.')
    n2 = texto.count('!')
    n3 = texto.count('?')
    return n1 + n2 + n3