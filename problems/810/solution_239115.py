def inverte(frase):
    """retorna frase na ordem inversa, sem letras maiusculas e sem pontuação.
    str->str"""
    a= str.replace(frase,'.',' ')
    b= str.replace(a,',',' ')
    c= str.replace(b,'-',' ')
    d= str.replace(c,':',' ')
    e= str.replace(d,';',' ')
    f= str.replace(e,'!',' ')
    g= str.replace(f,'?',' ')
    h= str.replace(g,'...',' ')
    
    x=str.split(h)
    
    return str.join(' ',x.reverse())