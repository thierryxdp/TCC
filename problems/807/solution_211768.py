def conta_frases('frase'):
    reticencias=str.count('frase','...')
    ponto=str.count('frase','.')-3*reticencias
    exclamacao=str.count('frase','!')
    interrogacao=str.count('frase','?')
    reticencias=str.count('frase','...')
    x=ponto+exclamacao+interrogacao+reticencias
    return x