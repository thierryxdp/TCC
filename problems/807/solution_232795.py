def conta_frases(frase):
    inter = str.count(frase,'?')
    escl = str.count(frase,'!')
    ponto = str.count(frase, '. ')
    pontos = str.count(frase, '...')
    final = 0
    if frase[-1] = '.':
        final = 1
    return inter+escl+ponto+pontos+final