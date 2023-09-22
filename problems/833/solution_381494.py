def conta_numero(numero,matriz):
    """Dado de entrada um número inteiro e uma matriz, 
    retorna quantas vezes esse número apareceu na matriz"""
    """int,list=>int"""
    n=0
    contador=0
    for i in matriz[n]:
    		contador=contador+list.count(i,numero)
    	n=n+1
  	return contador