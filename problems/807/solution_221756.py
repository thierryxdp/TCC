def conta_frases(frase):
    frase = str.replace(frase,'!','.') and str.replace(frase,'?','.') and str.replace(frase,'...','.')
    return len(str.split(frase,'.')) - 1