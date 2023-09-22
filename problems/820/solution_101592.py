def posLetra (frase,letra,numero):
    """
    	string,string,int -> int
    """
	ocorrencias = frase.count(letra)
    
        
    if ocorrencias<numero:
        return -1