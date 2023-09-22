def conta_frases(frase):
    'str ->int'
    f2=frase.replace(frase)
    frase.replace('?','.')
    frase.replace('!','.')
    frase.replace('...','.')
    return len(frase.strip().split('.'))-1