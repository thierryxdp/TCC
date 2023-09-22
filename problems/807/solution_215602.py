def conta_frases(frase):
    frase1 = str.partition(frase,'.')
    frase2 = str.partition(frase,'...')
    frase3 = str.partition(frase,'!')
    frase4 = str.partition(frase, '?')
    return len(frase)