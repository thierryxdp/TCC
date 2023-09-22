def faltante(n):
  	"""O tamanho da lista é N-1."""
  	"""O intervalo é sempre de 1 a N."""
  	"""Se o tamanho dela for 1, quer dizer que é 2-1."""
    """Então o intervalo dela é 1 a 2, ou 2 a 1."""
    peca_faltante = 0
  	if (len(n) == 1):
    	if (n[0] == 1):
    	  	peca_faltante = 2
    	if (n[0] == 2):
      		peca_faltante = 1
    	return peca_faltante
  	else:
  		n.sort()
  		if (n[0] != 1):
    		peca_faltante = 1
    		return peca_faltante
  		else:
    		i = 0
    		while i < len(n)-1: 
       			if n[i]+1 != n[i+1]:
            		peca_faltante = n[i]+1
       		i=i+1
    	if peca_faltante == 0:
      		peca_faltante = n[i] +1
    		return peca_faltante