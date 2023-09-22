def inverte(frase):
    """A função remove as pontuações da frase, substitui as letras maisculas
    por minusculas e inverte a frase:
    str -> str"""
    frase = frase.replace('-', ' ')
    frase = frase.replace(',', '')
    frase = frase.replace(':', '')
    frase = frase.replace(';', '')
    frase = frase.replace('.', '')
    frase = frase.replace('?', '')
    frase = frase.replace('!', '')
    frase = str.lower(frase)
    frase = frase.split()
    frase = " ".join(frase)
    return frase