def inverte (frase):
    """Funcao que inverte as palavras de uma frase"""
    """string -> string"""
    list.reverse(frase)

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