def conta_frases(frase):
    f2=frase.replace()
    frase.replace('?','.')
    frase.replace('!','.')
    frase.replace('...','.')
    return len(frase.strip().split('.'))-1