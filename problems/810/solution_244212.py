def inverte(frase):
    """funcao que dada uma frase retona ela invertida, com letras minusculas e invertida.
    str -> str"""
    frase = frase.lower()
    frase = frase.replace("-", " ")
    frase = frase.replace(",", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("?", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace("...", " ")
    frase = frase.split()
    frase.reverse()
    frase = tuple(frase)
    frase = str.join(" ", frase)
    return frase