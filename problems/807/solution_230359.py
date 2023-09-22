def conta_frases(frase):
    str.split(frase,'...')
    str.split(frase,'?')
    str.split(frase,'!')
    return len(str.split(frase,'...'))+len(str.split(frase,'?'))+len(str.split(frase,'!'))