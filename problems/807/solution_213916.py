def conta_frases(frase):
    a = frase
    a = str.replace(a,'...','#')
    a = str.replace(a,'!','#')
    a = str.replace(a,'?','#')
    a = str.replace(a,'.','#')
    return a.count('#')