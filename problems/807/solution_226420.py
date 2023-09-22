def conta_frases(frase):

    frase = frase.replace('!','.')
    frase = frase.replace('?','.')
    frase = frase.replace('...','.')
    nova_frase = frase.split('.')
    return len(nova_frase)-1