def conta_frases(frase):
    """"""
    frase1 = str.replace(frase, '!', '.')
    frase2 = str.replace(frase1, '?', '.')
    frase3 = str.replace(frase2, '...', '.')
    lista = str.split(frase3, '.')
    return len(lista)