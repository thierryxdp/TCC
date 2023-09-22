def faltante(quant):
    i=1
    while i < len(quant):
        if i not in quant[i]:
          	return i
    	i=i+1