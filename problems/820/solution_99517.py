def posLetra(texto,l,n):
    """ """
    if str.count(texto,l) < n:
        return -1
    else:
    	vzs = 0
    	resposta = 1
    	txt = texto
    	while vzs < n:
        	resposta += str.find (txt,l)  
        	vzs += 1
        	txt = txt[resposta:]
		return resposta