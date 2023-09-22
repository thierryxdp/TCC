def retira_pontuacao(frase):
    """
    Faca uma funcao que dada uma frase, substitua todos os pontos por espacos em braco,
    str -> str
    """
    frase = str.split(frase, "-")
    frase = str.join(" ", frase)
    frase = str.split(frase, ",")
    frase = str.join(" ", frase)
    frase = str.split(frase, ":")
    frase = str.join(" ", frase)
    frase = str.split(frase, ";")
    frase = str.join(" ", frase)
    frase = str.split(frase, ".")
    frase = str.join(" ", frase)
    frase = str.split(frase, "?")
    frase = str.join(" ", frase)
    frase = str.split(frase, "!")
    frase = str.join(" ", frase)
    return frase