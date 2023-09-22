def conta_frases(frase):
    frase.replace('?','/')
    frase.replace('!','/')
    frase.replace('.','/')
    frase.replace('...','/')
    nova=frase.split('/')
    return len(nova)