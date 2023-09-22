def conta_frases(frase):
    
    f= str.replace(frase,'...','.')
    fr= f + str.replace(frase,'.','.')
    fra=fr + str.replace(frase,'?','.')
    fras= fra + str.replace(frase,'!','.')
    frase=str.split(frase,'.')
    
    return len(frase)