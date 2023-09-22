def conta_numero(numero,matriz):
    """dado um número inteiro (numero) e uma matriz de inteiros (matriz), retorna quantas vezes esse número aparece na matriz,
    	(int,list) -> int"""
    contador=0
    for i in range(len(matriz)):
        x=list.count(matriz[i])
        contador=contador+x
    return contador