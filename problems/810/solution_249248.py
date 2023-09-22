def inverte(frase):
    """ """
    a=frase.replace("!"," ")
    
    b=a.replace("-"," ")
    
    c=b.replace(","," ")
    
    d=c.replace("."," ")
    
    e=d.replace("?"," ")
    
    f=e.replace("—"," ")
    
    g=f.replace(":"," ")
    
    h=g.replace(";"," ")
    
    if len(h)<=1:
        return h
    
    return h[1:] + h[0]