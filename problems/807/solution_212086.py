def conta_frases(texto):
    '''Dado um texto, a função retorna o número de frases dele.
    str -> int'''
    # como a quantidade de frases é igual a quantidade de pontuações, substituindo as pontuações por #, temos:
    texto_modificado = str.replace(texto, '...', '#')
    texto_modificado = str.replace(texto_modificado, '.', '#')
    texto_modificado = str.replace(texto_modificado, '!', '#')
    texto_modificado = str.replace(texto_modificado, '?', '#')
    palavras = str.count(texto_modificado, '#')
    return palavras