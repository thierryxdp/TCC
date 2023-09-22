def conta_frases(frase):
    import string
    pontuacao = string.punctuation
    for c in pontuacao:
        frase = frase.replace(c,7)
    return frase.count('7')