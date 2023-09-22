def conta_frases(texto):
    """
    
    """
    a=str.replace(texto,"...","#")
    b=str.replace(a,".","#")
    c=str.replace(b,"!","#")
    d=str.replace(c,"?","#")
    frases=str.split(d,"#")
    return len(frases)-1