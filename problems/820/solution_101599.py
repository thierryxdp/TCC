def posLetra (frase,letra,numero):
    """
    	string,string,int -> int
    """
    i = 0
	ocorrencias = frase.count(letra)
    if ocorrencias<numero:
        return -1
    while i<numero:
        frase = frase.find(letra)
        
    return frase