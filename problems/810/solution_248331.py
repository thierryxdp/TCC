def inverte(k):
        """inverte a ordem das palavras contidas numa frase"""
        
    a=k.replace("!"," ")
    
    b=a.replace("-"," ")
    
    c=b.replace(","," ")
    
    d=c.replace("."," ")
    
    e=d.replace("?"," ")
    
    f=e.replace("—"," ")
    
    g=f.replace(":"," ")
    
    h=g.replace(";"," ")
    
    x=h.split(" ")
    
    len(x)=i

    return x[::-1]