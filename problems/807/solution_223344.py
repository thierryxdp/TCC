def conta_frases(texto):
    '''Conta e retorna o número de frases existentes no
       texto de entrada;
       str -> int'''
    return texto.count('.')+texto.count('!')+texto.count('...')