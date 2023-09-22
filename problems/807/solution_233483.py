def conta_frases(frase):
    conta=frase.count('!')
    conta2=frase.count('?')
    conta3=frase.count('...')
    conta4=frase.count('.')-conta3*3
    return conta+conta2+conta3+conta4