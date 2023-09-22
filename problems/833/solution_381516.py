def conta_numero(numero,matriz):
    """Dado de entrada um número inteiro e uma matriz, 
    retorna quantas vezes esse número apareceu na matriz"""
    """int,list=>int"""
    contador=0
    for i in matriz:
    	for j in i:
            if j==numero:
            contador=contador+1
    return contador