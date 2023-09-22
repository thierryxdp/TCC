def conta_frases(texto):
    '''Dado um texto, retorna quantas frases há nele.
    str -> int'''
    texto = texto.replace('!','.')
    texto = texto.replace('?','.')
    texto = texto.replace('...','.')
    texto_lista = texto.split('.')
    return len(texto_lista)