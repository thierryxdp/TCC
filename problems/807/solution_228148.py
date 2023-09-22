def conta_frases(texto):
    '''Retorna quantas frases existem no texto recebido'''
    frase = texto
    frase = str.replace (frase, '...', '.')
    return str.count (frase, '.') + str.count (frase, '?') + str.count (frase, '!')