def conta_frases(texto):
    contador = ()
    pontos = '(...)!?.'
    for palavras in texto:
        if palavras in pontos:
            contador = contador + tuple(palavras)
    return len(contador)