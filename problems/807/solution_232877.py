def conta_frases(frase):
    '''retornas o numero de frases q aparece no texto str-> int'''
    ponto = frase.split('.')
    excl = frase.split('!')
    inter =frase.spli('?')
    retic = frase.count('...')
    
    return (len(ponto) - 2*retic) + len(excl) + len(inter)