def eh_quadrada(matriz):
    '''Função que, dada uma matriz, identifica se ela é quadrada ou não e retorna um valor booleano.
    list -> bool'''
    for i, linha in enumerate(matriz):
        if len(linha) != len(matriz):
            return False
        else:
            return True
        for j in range(i):
            if linha[j] != matriz[j][i]:
                return False
    return True