def posLetra(texto,l,n):
    """ """
    if str.count(texto,l) < n:
        return -1
    else:
    	vzs = 0
    	resposta = 0
    	txt = texto
    	while vzs < n:
        	resposta += str.find (txt,l)  
        	vzs += 1
        	txt = txt[resposta:]
		if texto[0] == l:
        	return resposta -1
        else:
            return resposta -1