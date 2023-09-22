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
    
    x=(h.split(" "))
    
     if len(x)<=1:
            return x
        
        return x[1:] + x[0]