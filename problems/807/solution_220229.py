def conta_frases(frase):
    f2=frase.replace('?','.')
    f2=f2.replace('!','.')
    f2=f2.replace('...','.')
    return len(f2.strip().split('.'))-1