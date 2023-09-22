def conta_frases(frase):
    nfrase = frase.replace("...", ".")
    final1 = nfrase.count('.')
    final2 = nfrase.count('!')
    final3 = nfrase.count('?')
    resultado = final1+final2+final3
    return resultado