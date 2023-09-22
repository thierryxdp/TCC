def conta_numero(numero,matriz):
    """dado um número inteiro(numero) e uma matriz de inteiros(matriz), retorna quantas vezes o número de entrada aparece na matriz,
		(int,list) -> int"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            contador = list.count(matriz[i][j],numero)
   	print contador