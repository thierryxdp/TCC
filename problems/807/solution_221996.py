def conta_frases(texto):
    """conta o numero de frases que aparecem em um dado
    texto (determinadas por . ou ! ou ? ou ...)
    str -> int"""
    texto2=str.strip(texto,"...")
    texto3=str.strip(texto2,"?")
    texto4=str.strip(texto3,"!")
    texto5=str.strip(texto4,".")
    
    x = str.split(texto5)
    
    return len(x)