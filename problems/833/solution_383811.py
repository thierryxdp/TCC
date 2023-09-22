def conta_numero(numero,matriz):
    vezes=0
    i=0
    while i<len(matriz):
        vezes=vezes+list.count(matriz[i],numero)
    	i=i+1
   	return vezes