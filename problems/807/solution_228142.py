def conta_frase(texto):
    '''Retorna quantas frases existem no texto recebido'''
    texto = frase
    frase = str.replace (frase, '...', '.')
    return str.count (frase, '.') + str.count (frase, '?') + str.count (frase, '!')