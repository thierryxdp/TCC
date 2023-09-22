def conta_frases(texto):
    contador = ()
    pontos = '.!?'
    for palavras in texto:
        if palavras in pontos:
            return palavras.count()