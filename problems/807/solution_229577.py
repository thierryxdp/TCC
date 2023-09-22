def conta_frases(texto):
    """
    	Funcao que dada uma frase, retorna o numero de palabras 
        da frase.
    """
    t = texto
    n = t.split(". ", "! ", "? ", "... ")
    return len(n)