def conta_frases(frase):
    'str ->int'    
    frase.replace('?','.')
    frase.replace('!','.')
    frase.replace('...','.')
    return len(frase.strip().split('.'))-1