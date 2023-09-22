def busca(setor,M):
    '''
    funcao que busca os dados de um funcionario de um setor em uma matriz de informacoes
    parametros:
    setor--->str
    M--->list
    saida:
    list
    '''
    funcionarios=[]
    i=0
    while i<len(M):
        if M[i][2]==setor:
            funcionarios.append(M[i])
        i+=1
    return funcionarios