def conta_frases(frase):
    pontoFinal = frase.replace(".","@")
    exclamacao = pontoFinal.replace("!","2")
    interrogacao = exclamacao.replace("?","@")
    reticencias = interrogacao.replace("...","@")
    return reticencias.count("@")