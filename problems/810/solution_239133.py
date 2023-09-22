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
    
    i= str.lower(h)
    
    x=str.split(i)
  
    
    y= str.join(' ',x)
    
    return y