def eh_quadrada(M):
    '''
    funcao que verifica se uma matriz e quadrada
    parametros:
    M--->list
    saida:
    bool
    '''
    if M==[]:
        return M==[]
    return len(M[0])==len(M)