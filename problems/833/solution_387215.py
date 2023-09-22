def conta_numero(numero,matriz):
    """Recebe um número que se deseja saber se ele se encontra numa matriz e a determinada matriz e devolve e quantidade de vezes que esse numero aparece;
    	int, list -> int"""
    qtd=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                qtd=qtd+1
    return qtd