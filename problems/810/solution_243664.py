def inverte(frase):
    a=str.replace(frase,'-',' ')
    b=str.replace(a,':',' ')
    c=str.replace(b,',',' ')
    d=str.replace(c,';',' ')
    e=str.replace(d,'.',' ')
    f=str.replace(e,'?',' ')
    g=str.replace(f,'!',' ')
    h=str.replace(g,'...',' ')
    i=str.lower(h)
    j=str.split(i)
    k=str.join(frase,j)
    return k