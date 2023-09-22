def conta_frases(frase):
    ponto_final = frases.replace("...", '@')
    ponto_exclamacao = ponto_final.replace("!", '@')
    ponto_interrogacao = ponto_exclamacao.replace("?", '@')
    reticencias = ponto_interrogacao.replace(".", '@')
    return reticencias.count('@')