def conta_frases(frase):
    frase=str.replace('!','/')
    frase=str.replace('...','/')
    frase=str.replace('.','/')
    frase=str.replace('?','/')
    texto=str.split(frase,'/')
    numero=len(texto)-1
    return numero