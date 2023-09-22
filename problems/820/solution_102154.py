def posLetra(string,letra,ocorrencia):
  	i = 0
  	l = 0
    while i<= ocorrencia :
        if letra == string[l]:
        	i = i+1
            l = l+1
        else:
            l = l+1
            
   	return l