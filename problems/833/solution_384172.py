def conta_numero(numero,matriz):
    """
    Conta quantas vezes determinado numero aparece na matriz
    
Parametros:
	numero:int,
    numero desejado para a procura.
    
    matriz:list,
    matriz a sua escolha
"""
    soma=0
    sequencia=0
    for sequencia in range(len(matriz)):
        contador=matriz[sequencia].count(numero)
        soma+=contador
	return soma