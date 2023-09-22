def conta_numero(N, matriz):
    '''
        recebe uma matris e um numero e retorno quantas vezes esse numero dado
        e encontrado nessa matriz
        entrada: lista, interiro
        saida: interiro
    '''
    qtd_num = 0
    if (matriz == []):
        return qtd_num
    else:
        linha = len(matriz)
        coluna = len(matriz[0])
        for i in range(linha):
            for j in range(coluna):
                if N == matriz[i][j]:
                    qtd_num = qtd_num + 1
        return qtd_num