def conta_frases(frase):
    exc = frase.count('!')
    inter = frase.count('?')
    etc = frase.count('...')
    fin = frase.count('.') - 3 * etc
    return exc + inter + etc + fin