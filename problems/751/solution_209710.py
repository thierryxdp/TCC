def quant_palavras(frase):
    pontoFinal = frases.replace("...", '@')
    exclamacao = pontoFinal.replace("!", '@')
    interrogacao = exclamacao.replace("?", '@')
    reticencias = interrogacao.replace(".", '@')
    return reticencias.count('@')