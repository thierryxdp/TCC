def conta_frases(frases):
    """
    Dada uma frase, conta quantos pontos de interrogação, exclamação, final há numa frase.
    :param frases: str -> str
    :return: int -> int
    """
    pontoFinal = frases.replace("...", '_')
    pontoExclamacao = pontoFinal.replace("!", '_')
    pontoInterrogacao = pontoExclamacao.replace("?", '_')
    reticencias = pontoInterrogacao.replace(".", '_')
    return reticencias.count('_')