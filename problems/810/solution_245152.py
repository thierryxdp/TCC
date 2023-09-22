def inverte(frase):
    """Essa função dada uma frase, retorna outra frase que contenha as mesmas palavras na ordem inversa, sem letras maiúsculas e sem pontuação"""
    frase = frase.replace("-", " ")
    frase = frase.replace(",", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace("?", " ")
    frase = str.lower(frase)
    frase = str.split(frase)
    frase = frase[::-1]
    frase = " ".join(frase)
    return frase