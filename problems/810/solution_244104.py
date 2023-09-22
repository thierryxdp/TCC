def inverte(frase):
    '''Inverte a ordem das palavras de uma frase.
    STR->STR'''
    frase = frase.lower()
    frase = frase.replace("-", " ")
    frase = frase.replace(",", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace("?", " ")
    frase = frase.replace("...", " ")
    frase = frase.split()
    frase.reverse()
    frase = tuple(frase)
    frase = str.join(" ", frase)
    return frase