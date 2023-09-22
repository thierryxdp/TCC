def conta_frases(frase):
    n1 = frase.count('.')
    n2 = frase.count('!')
    n3 = frase.count('?')
    n4 = frase.count('...')
    return len(n1)