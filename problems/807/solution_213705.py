def conta_frases(frase):
    pontoFinal = frases.replace("...", ' ')
    pontoExclamacao = pontoFinal.replace("!", ' ')
    pontoInterrogacao = pontoExclamacao.replace("?", ' ')
    reticencias = pontoInterrogacao.replace(".", ' ')
    return reticencias.count(' ')
print (conta_frases)