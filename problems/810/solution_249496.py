def inverte(frase):
    
    """inverte a ordem das palavras de uma frase"""
    
    a=frase.replace("!"," ")
    
    b=a.replace("-"," ")
    
    c=b.replace(","," ")
    
    d=c.replace("."," ")
    
    e=d.replace("?"," ")
    
    f=e.replace("—"," ")
    
    g=f.replace(":"," ")
    
    h=g.replace(";"," ")
    
    frase_nova=sorted(h, reverse=True)
    
    return h