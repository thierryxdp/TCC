def conta_frases(frase):
    frase = str.replace(frase,'!','.') 
    frase = str.replace(frase,'?','.') and str.replace(frase,'...','.')
    split = str.split(frase,'.')
    if (frase[-1] == '.'):
        return len(split) - 1
    else:
        return len(split)