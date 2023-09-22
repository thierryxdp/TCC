def conta_frases(frase):
    '''retorna o numero de frases que aparece no texto
    str->int'''
    ponto = frase.split('.')
    excl = frase.split('!')
    inter = frase.split('?')
    retic = frase.count('...')
    return (len(ponto) - 4*retic) + len(excl) + len (inter)