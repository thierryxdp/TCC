def conta_frases(frase):
    interrogacao=frase.count('?')
    exclamacao=frase.count('!')
    ponto=frase.count('.')
    reticencia=frase.count('...')
    return interrogacao + exclamacao + reticencia + ponto - 3*reticencia