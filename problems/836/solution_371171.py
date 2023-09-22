def busca(nome,matriz):
    '''Função que busca os dados de um funcionário através de 
    seu setor no trabalho.
    Parâmetros: list _> list'''
    nlin = len(matriz)
    ncol = len(matriz[0])
    C = []
    i = 0
    for i in range(nlin):
        for j in range(ncol):
            if nome == matriz[i][j]:
                C.append(matriz[i])
    i = 0
    while i < len(C):
        del C[i][2]
        i= i + 1                    
    return C