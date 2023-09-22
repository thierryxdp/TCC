def conta_frases(frase):
    a=str.replace(frase,'!','.')
    b=str.replace(a,'?','.')
    c=str.replace(b,'...','.')
    d=str.split(c,'.')
    
    return len(d)