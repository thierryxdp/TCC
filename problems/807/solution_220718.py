def conta_frases(frase):
    frase=frase.replace('...','/')
    frase=frase.replace('?','/')
    frase=frase.replace('.','/')
    frase=frase.replace('!','/')
    frase.split('/')
    return len(frase.split('/'))