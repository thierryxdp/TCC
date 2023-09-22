def conta_frases(frase):
    texto=frase.replace('?','/')
    texto=frase.replace('!','/')
    texto=frase.replace('.','/')
    texto=frase.replace('...','/')
    nova=frase.split(texto,'/')
    return len(nova)