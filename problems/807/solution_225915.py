def conta_frases(frase):
    """"""
    str.replace(frase, '!', '.')
    str.replace(frase, '?', '.')
    str.replace(frase, '...', '.')
    lista = str.split(frase, '.')
    return lista