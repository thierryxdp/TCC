def conta_frases(frase):
    inter = str.count(frase,'?')
    escl = str.count(frase,'!')
    ponto = str.count(frase, '. ')
    pontos = str.count(frase, '...')
    return inter+escl+ponto+pontos