def quant_palavras(frase):
    pontoFinal = frase.replace(".","#")
    exclamacao = pontoFinal.replace("!","#")
    reticencias = exclamacao.replace("...","#")
    interrogacao = reticencias.replace("?","#")
    return interrogacao.count("#")