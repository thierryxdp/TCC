def faltante(quant):
    i=0
    while i < len(quant):
        if quant[i] != i+1:
          	return i
        else:
            return i+1
        i=i+1