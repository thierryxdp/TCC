def posLetra (frase,letra,numero):
    """
    	string,string,int -> int
    """
    i = 0

    while i<numero:
        frase = frase.find(letra)
        return frase