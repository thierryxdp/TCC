def conta_frases (frase):
    contagem = ()
    if '! ' in frase:
        return contagem + str.replace(frase, '! ', ' ')