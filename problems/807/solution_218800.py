def conta_frases (frase):
    contagem = list()
    if '! ' in frase:
        return list() + str.replace(frase, '! ', ' ')