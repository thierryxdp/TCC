def conta_frases(frases):
    "Essa funcao conta o numero de frases que aparecem no texto, recebido no parametro."
    pontoFinal=frases.replace("...",'_')
    pontoExclamacao=pontoFinal.replace("!",'_')
    pontoInterrogacao=pontoExclamacao.replace("?",'_')
    reticencias=pontoInterrogacao.replace(".",'_')
    return reticencias.count('_')