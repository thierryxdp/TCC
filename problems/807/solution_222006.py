def conta_frases(texto):
    """conta o numero de frases que aparecem em um dado
    texto (determinadas por . ou ! ou ? ou ...)
    str -> int"""
    
    x = int(str.count(texto,"..."))
    
    texto2=str.replace(texto,"..."," ")

    x+=int(str.count(texto2,"?"))
    x+=int(str.count(texto2,"!"))
    x+=int(str.count(texto2,"."))
        
    return int(x)