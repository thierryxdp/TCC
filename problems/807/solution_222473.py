def conta_frases (frase):
    '''
    	essa função receber uma entrada e calcula a quantidade total de frases presentes no total
        str -> int
    '''
    if '.' or '!' or '?' in frase:
        frase = str.replace(frase, '...','.')
    return str.count(frase, '.') + str.count(frase, '!') + str.count(frase, '?')