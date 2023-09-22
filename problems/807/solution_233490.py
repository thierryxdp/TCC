def conta_frase(frase):
    ponto = frase.split('.')
    excl = frase.split('!')
    inter = frase.split('?')
    retic = frase.count('...')
    return (len(ponto) - 2*retic) + len(excl) + len(inter)