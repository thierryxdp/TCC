def conta_frases(texto):
    '''Conta e retorna o número de frases existentes no
       texto de entrada;
       str -> int'''
    totalPts=texto.count('.')+texto.count('!')+texto.count('?')+texto.count('...')
    if '...' in texto:
        return totalPts - 3*texto.count('...')
    return totalPts