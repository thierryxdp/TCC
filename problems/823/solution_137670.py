def faltante(quant):
    i=1
    cont = 0
    while i < len(quant):
        if quant[i] != i+1:
          	return i
    	i=i+1