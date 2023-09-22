def conta_frases (frase):
    contagem = tuple()
    if '! ' in frase:
        return contagem + str.replace(frase, '! ', ' ')