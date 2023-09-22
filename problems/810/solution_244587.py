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
    frase = list.reverse(frase)
    return frase