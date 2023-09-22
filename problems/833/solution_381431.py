def conta_numero(numero,matriz):
    ''' funcao que dado uma matriz e um numero
    retorna quntas vezes esse numero aparece
    na matriz; int,list -> int'''
    qtd = 0
    if len(matriz) == 0:
        return 0  
    
    else:
        linhas = len(matriz)
        colunas = len(matriz[0])
        for i in range(linhas):
            for j in range(colunas):
                if matriz[i][j] == numero:
                    qtd = qtd + 1
        return qtd