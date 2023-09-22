def posLetra(texto,l,n):
    """retorna a posição da ocorrência n da substring l dentro da string texto
    str,str,int -> int"""
    if str.count(texto,l) < n:
        return -1
    else:
    	vzs = 0
    	resposta = 0
    	txt = texto
    	while vzs < n:
        	resposta += str.find (txt,l) + 1 
        	vzs += 1
        	txt = texto[resposta:]
		if texto[0] == l:
        	return resposta -1
        else:
            return resposta -1