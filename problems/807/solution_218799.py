def conta_frases (frase):
    contagem = list()
    if '! ' in frase:
        return contagem + str.replace(frase, '! ', ' ')