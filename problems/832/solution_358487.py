def eh_quadrada(lista):
    if lista!=[]: 
        n_linha=(len(lista))
        n_col=(len(lista[0]))
        if n_linha==n_col:
            return True
    	if n_linha!=n_col:
        	return False
  	else:
        return True