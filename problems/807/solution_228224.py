def conta_frases(texto):

    """conta o numero de frases terminadas por ".","...","!","?" 
    de um texto"""
      
    texto.replace("...","x")
    
    return len(texto.split("."))+len(texto.split("?"))+len(texto.split("x"))+len(texto.split("!"))