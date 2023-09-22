def conta_frases1(texto): 
    """funcao que conta o numero de frases que um texto contem;
       str->int"""
    texto.replace("...", "  ")
    texto=texto.replace("...", "  ")
    texto.replace("!","  ") 
    texto=texto.replace("!","  ")
    texto.replace("?"," ")
    texto=texto.replace("?","  ")
    texto.replace(".", "  ")
    texto=texto.replace(".", "  ")
    return len(texto.split("  ")[:-1])