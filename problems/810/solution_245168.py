def inverte (frase):
    """Função que retornar uma frase em que todos os caracteres de pontuação são substituídos por espaço"""
    """string -> string """
    frase = str.split(frase, ",")
    frase = str.join(" ", frase)
    frase = str.split(frase, ".")
    frase = str.join(" ", frase)
    frase = str.split(frase, "-")
    frase = str.join(" ", frase)
    frase = str.split(frase, ":")
    frase = str.join(" ", frase)
    frase = str.split(frase, ";")
    frase = str.join(" ", frase)
    frase = str.split(frase, "!")
    frase = str.join(" ", frase)
    frase = str.split(frase, "?")
    frase = str.join(" ", frase)
    return frase

def inverte (frase):
    """Função que inverte a ordem das palavras de uma frase"""
    """string -> string"""
    palavras = frase.split()
    palavras = list(reversed(palavras)
    return (" ".join(palavras))