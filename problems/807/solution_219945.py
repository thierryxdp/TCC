def conta_frases(frase):
    frase=str.strip(frase)
    frase=frase.replace(".","]")
    frase=frase.replace("!","]")
    frase=frase.replace("?","]")
    frase=frase.replace("...","]")
    aux=frase.split("]")
    return len(aux)0