def conta_frases(frase):
    a=str.replace(frase,'...',' ')
    b=str.replace(a,'?',' ')
    c=str.replace(b,'!',' ')
    d=str.replace(d,'.',' ')
    return len(str.split(d,'  '))