#conta frases
def conta_frases(texto):
    """funcao que conta o numero de frases em um texto.
       str-->int"""
    Int=texto.count("?")
    Ponto=texto.count(".")
    Exc=texto.count("!")
    Ret=texto.count("...")
    return (Int+Ponto+Exc+Ret)