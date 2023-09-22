def inverte(frase):
    "Funcao que inverte a ordem das palavras na frase dada"
    a= str.replace(frase,'-',' ')
    b= str.replace(a,',',' ')
    c= str.replace(b,':',' ')
    d= str.replace(c,';',' ')
    e= str.replace(d,'.',' ')
    f= str.replace(e,'!',' ')
    g= str.replace(f,'?',' ')
    frasenova = g
    invert = frasenova
    f = str.split(invert)
    return str.lower(str.join(' ',f[::-1]))