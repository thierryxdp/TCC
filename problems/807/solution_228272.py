def conta_frases(texto):
    """determina o numero de frases"""
    
    
    texto.replace("...","x")
    
    a=texto.split(".")
    b=texto.split("!")
    c=texto.split("?")
    d=texto.split("x")
    
    if len(a[0:1]<=1 
    
    return 1+len(b[0:1])+len(c[0:1])+len(d[0:1])