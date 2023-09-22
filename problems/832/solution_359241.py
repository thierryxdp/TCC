def eh_quadrada(M):
    '''
    funcao que verifica se uma matriz e quadrada
    parametros:
    M--->list
    saida:
    str
    '''
    if M==[]:
        return 'True'
    if len(M[0])==len(M):
        return 'True'
    else:
        return 'False'