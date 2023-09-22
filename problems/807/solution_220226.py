def conta_frases(frase):
    'str ->int'
    f2=f2.replace('?','.')
    f2=f2.replace('!','.')
    f2=f2.replace('...','.')
    return len(f2.strip().split('.'))-1