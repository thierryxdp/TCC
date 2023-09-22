def conta_frases(frase):
    '''função que retorna o número de fraes que aparecem num texto, considerando que cada frase termina em '!', '.', '...' ou '?'.
    entrada: string
    saída: int'''
    
    return str.count(frase, '.') + str.count(frase, '...') + str.count(frase,'?') + str.count(frase, '!')