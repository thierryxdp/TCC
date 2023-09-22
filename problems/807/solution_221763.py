def conta_frases(frase):
    frase = str.replace(frase,'!','.') 
    frase = str.replace(frase,'?','.') and str.replace(frase,'...','.')
    split = str.split(frase,'.')
    return len(split)