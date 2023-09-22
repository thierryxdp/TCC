def posLetra(texto,l,n):
    """ """
    if str.count(texto,l) < n:
        return -1
    else:
    	vzs = 0
    	resposta = 0
    	txt = texto
    	while vzs < n:
        	resposta += str.find (txt,l) + 1 
        	vzs += 1
        	txt = txt[resposta:]
		
            return resposta -1