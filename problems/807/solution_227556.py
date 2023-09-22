def conta_frases(frase):
    pontoFinal = frase.replace("...", '@')
    exclamacao = pontoFinal.replace("!", '@')
    interrogacao = exclamacao.replace("?", '@')
    reticencias = ponto_interrogacao.replace(".", '@')
    return reticencias.count('@')