def conta_frases(frase):
    frase = str.replace(frase,'!','.') 
    frase = str.replace(frase,'?','.') and str.replace(frase,'...','.')
    return len(str.split(frase,'.'))