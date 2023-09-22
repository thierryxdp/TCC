def conta_frases(frase):
    frase = str.split(frase,'.'), str.split(frase,'!'), str.split(frase,'?'), str.split(frase,'...')
    return len(frase)