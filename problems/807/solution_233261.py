def conta_frases(texto):
    pontos = '.!?'
    for palavras in texto:
        if palavras in pontos:
            return palavras