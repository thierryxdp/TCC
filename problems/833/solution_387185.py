def conta_numero(numero,matriz):
    i=0
    c=0
    while i<len(matriz):
    	c=c+list.count(matriz[i],numero)
        i=i+1
    return  c