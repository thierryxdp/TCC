def conta_frases(frase):
    import string
    pontuacao = string.punctuation
    for c in pontuacao:
        frase = frase.replace(c,'')
    return frase.count('')