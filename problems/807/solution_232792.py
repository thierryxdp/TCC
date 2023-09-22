def conta_frases(frase):
    inter = str.count(frase,'?')
    escl = str.count(frase,'!')
    ponto = str.count(frase, '. ')
    3_pontos = str.count(frase, '...')
    retunr inter+escl+ponto+3_pontos