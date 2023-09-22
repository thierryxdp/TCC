def conta_frases(texto):
    '''Esta funcao conta o numero de frases que aparecem em um texto.'''
    '''str --> int'''
    texto = str.strip(texto, ' ')
    texto_dividido = str.split(texto, '(.)(!)(?)(...) ')
    qtd = len(texto_dividido)
    return qtd