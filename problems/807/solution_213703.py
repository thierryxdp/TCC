def conta_frases(frase):
    pontoFinal = frases.replace("...", '_')
    pontoExclamacao = pontoFinal.replace("!", '_')
    pontoInterrogacao = pontoExclamacao.replace("?", '_')
    reticencias = pontoInterrogacao.replace(".", '_')
    return reticencias.count('_')