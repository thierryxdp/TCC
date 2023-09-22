def conta_frases(frase):
    import string
    pontuacao = string.punctuation
    for x in pontuacao:
        frase = frase.replace(x,'  ')
    return frase.count('  ')