def conta_numero(numero,M):
    '''
    funcao que recebe um numero inteiro e uma matriz M
    de qualquer tamanho e retorna quantas vezes esse
    numero inteiro aparece na matriz
    int,list->int
    '''
    i=0
    for m in range(0, len(M)):
        for n in range(0, len(M[m])):
            if M[m][n]==numero:
                i=i+1
    return i