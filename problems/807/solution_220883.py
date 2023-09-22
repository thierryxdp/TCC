def conta_frases(texto):
    '''Dado um texto, retorna quantas frases há nele.
    str -> int'''
    texto_lista=texto.split('.','!','?','...')
    return len(texto_lista)