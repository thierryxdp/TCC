def conta_frases(texto): 
    """funcao que conta o numero de frases que um texto contem;
       str->int"""
    texto.split(".")
    texto=texto.split(".")[1]
    texto.split("!") 
    texto=texto.split("!")[1] 
    texto.split("?")
    texto=texto.split("?")[1]
    texto.split("...")
    return len(texto.split())