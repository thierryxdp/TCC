def conta_frases(frase):
    a=str.replace(frase,'!','.')
    b=str.replace(a,'?','.')
    c=str.replace(b,'...','.')
    
    return len(str.split(d,'.'))-1