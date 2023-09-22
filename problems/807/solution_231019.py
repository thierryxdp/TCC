def conta_frases(frase):
    a=str.replace(frase,'...','xpto')
    b=str.replace(a,'?','xpto')
    c=str.replace(b,'!','xpto')
    d=str.replace(c,'.','xpto')
    return len(str.split(d,'xpto'))-1