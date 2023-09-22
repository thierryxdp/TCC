def conta_numero(numero, matriz):
    ''' função que dado um número inteiro e uma matriz de int
    	conta e retorna quantas vezes aquele número apareceu
        na matriz.
        int, list(list) ---> int '''
    linhas = len(matriz)
    colunas = len(matriz[0])
    repeticoes = 0
    for a in colunas:
        if numero in matriz[0] or in matriz[1]:
            repeticoes = repeticoes + list.count(matriz[0], numero) + list.count(matriz[1], numero)