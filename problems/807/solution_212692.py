def conta_frases(texto):
    frase =str.count(frase,'.')
    frase2 =str.count(frase,'!')
    frase3 =str.count(frase,'?')
    frase4 =str.count(frase,'...')
    return len(texto[frase])+len(texto[frase2])+len(texto[frase3])+len(texto[frase4]