def conta_frases(texto):
    """
    	Funcao que dada uma frase, retorna o numero de palabras 
        da frase.
    """
    a = texto
    b = a.split(". ")
    c = b.split("!")
    d = c.split("? ")
    e = d.split("... ")
    return len(e)