def conta_frases(texto):
    """
    	Funcao que dada uma frase, retorna o numero de palabras 
        da frase.
    """
    a= str.count(texto,". ")
    b= str.count(texto,"! ")
    c= str.count(texto,"? ")
    d= str.count(texto,"... ")
    return a+b+c+d