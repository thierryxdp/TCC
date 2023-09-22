def conta_frases(frase):
    'str ->int'
    f2=frase.replace()
    frase.replace('?','.')
    frase.replace('!','.')
    frase.replace('...','.')
    return len(f2.strip(f2).split('.'))-1