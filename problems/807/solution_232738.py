def conta_frases(frase):
    frase=str.replace(frase,'!','/')
    frase=str.replace(frase,'...','/')
    frase=str.replace(frase,'.','/')
    frase=str.replace(frase,'/')
    texto=str.split(frase,'/')
    numero=len(texto)-1
    return frase