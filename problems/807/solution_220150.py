def conta_frases(frase):
    'str ->int'    
    frase.replace('?','.')
    frase.replace('!','.')
    frase.replace('...','.')
    f2=frase.replace()
    return len(f2.strip().split('.'))-1