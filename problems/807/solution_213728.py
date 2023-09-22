def conta_frases(frase):
    #Essa função determina o número de frases em um texto a partir da pontuação como exclamação, interrogação, ponto final
    PontoFinal = frase.replace("...","_")
    PontoExclamacao = PontoFinal.replace("!", '_')
    PontoInterrogacao = PontoExclamacao.replace("?", '_')
    Reticencias = PontoInterrogacao.replace(".", '_')
    return Reticencias.count('_')