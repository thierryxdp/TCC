def conta_frases(texto):
    '''Retorna a quantidade de frases presente no texto inserido como parâmetro.
    str->int'''
    texto_sem_reticencias=str.replace(texto,'...','.')
    return str.count(texto_sem_reticencias,'.')+str.count(texto,'?')+str.count(texto,'!')