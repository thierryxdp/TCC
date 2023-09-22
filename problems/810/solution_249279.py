def inverte(frase):
    
    
    a=frase.replace("!"," ")
    
    b=a.replace("-"," ")
    
    c=b.replace(","," ")
    
    d=c.replace("."," ")
    
    e=d.replace("?"," ")
    
    f=e.replace("—"," ")
    
    g=f.replace(":"," ")
    
    h=g.replace(";"," ")
    
    h.split(" ")
    
    h.sort(reverse=True)
    
    return h