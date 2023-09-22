def media_matriz(M):
    '''
    funcao que calcula a media dos termos de uma matriz
    parametros:
    M--->list
    saida:
    float
    '''
    i=0
    soma_linhas=[]
    while i<len(M):
        soma_linhas.append(sum(M[i]))
        i+=1
    return round(sum(soma_linhas)/(len(M)*len(M[0])),2)