def eh_quadrada(mat):
    for i, linha in enumerate(mat):
        if len(linha) != len(mat): # tamanho diferente, não é matriz quadrada
            return False # então não pode ser simétrica
        for j in range(i):
            if linha[j] != mat[j][i]:
                return False
    return True