def conta_frases(frase):
    reticencias=frase.count('...')
    ponto=frase.count('.')-reticencias*3
    return frase.count('!')+frase.count('?')+reticencias+ponto