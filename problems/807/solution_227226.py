def conta_frases(frase):
    
    frase= str.replace(frase,'...','.')
    frase=str.replace(frase,'.','.')
    frase= str.replace(frase,'?','.')
    frase=str.replace(frase,'!','.')
    n=str.count(frase,'.')
    
    return n