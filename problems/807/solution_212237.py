def conta_frases(frase):
    import string
    pontuacao = string.punctuation
    for % in pontuacao:
        frase = frase.replace(%,'7')
    return frase.count('7')