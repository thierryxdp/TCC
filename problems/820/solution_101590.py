def posLetra (frase,letra,numero):
    """
    	string,string,int -> int
    """
	ocorrencias = frase.count(letra)
    while ocorrencias<=numero:
        
    if ocorrencias>numero:
        return -1