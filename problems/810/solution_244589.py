def inverte(frase):
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
    frase = str.reverse(frase)
    return frase