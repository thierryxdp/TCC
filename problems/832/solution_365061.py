def eh_quadrada(M):
    '''Função que dada uma matriz, verifica se é uma 
    matriz quadrada
    matriz -> bool'''
    for i in range(len(M)):
        for j in range(len(M[0])):
            if len(M) == len(M[0]):
                return True
            if M[i][j] != M[j][i] or M[j] != M[j][i]:
                return False
    return True