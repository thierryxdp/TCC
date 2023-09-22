def conta_frases(frase):
    ponto=str.count('frase','.')
    exclamacao=str.count('frase','!')
    interrogacao=str.count('frase','?')
    reticencias=str.count('frase','...')
    x=ponto+exclamacao+interrogacao+reticencias
    return x