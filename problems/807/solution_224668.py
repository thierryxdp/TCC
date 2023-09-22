def conta_frases(frase):
    str.replace(frase,'...','/')
    str.replace(frase,'.','/')
    str.replace(frase,'?','/')
    str.replace(frase,'!','/')
    return len(str.split(frase,'/'))