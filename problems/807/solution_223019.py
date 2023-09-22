def conta_frases(frases):
    """
    Dada uma frase, conta quantos pontos de interrogação,
    exclamação, final há numa frase.
    str -> int
    """
    PontoFinal = frases.replace(".", '_')
    PontoExclamacao = PontoFinal.replace("!", '_')
    PontoInterrogacao = PontoExclamacao.replace("?", '_')
    Reticencias = PontoInterrogacao.replace("...", '_')
    return Reticencias.count('_')