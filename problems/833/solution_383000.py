conta_numero(numero,matriz):
    """Dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, 
    retorna quantas vezes aquele numero aparece na matriz.
    int, list -> int"""
    qtd = 0
    for i in matriz:
        for j in i:
            if numero == j:
                qtd += 1
	return qtd