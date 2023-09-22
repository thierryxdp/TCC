def conta_frases(frase):
    numero1 = str.(frase.count('.'))
    numero2 = str.(frase).count('!')
    numero3 = str.(frase).count('?')
    numero4 = str.(frase).count('...')
    return len(numero1)