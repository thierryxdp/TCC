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
    
    ximbinha=(h.split(" "))
    
     if len(ximbinha)<=1:
            return ximbinha
        
        
        return ximbinha[1:] + ximbinha[0]