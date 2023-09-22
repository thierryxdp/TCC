def conta_numero(numero,matriz):
    """Dado de entrada um número inteiro e uma matriz, 
    retorna quantas vezes esse número apareceu na matriz"""
    """int,list=>int"""
    n=0
    contador=0
    for i in matriz:
    	for j in len(i):
            contador=contador+list.count(matriz[i],numero)
    	n=n+1
    return contador