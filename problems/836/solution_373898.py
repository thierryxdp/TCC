def busca(s,A):
    '''
    	A função recebe uma string (nome do setor) e uma matriz A ao qual cada 
        linha contém as informações de um funcionário em strings (nome, registro, 
        setor e número; respectivamente). Com isso, ela retorna unova ma matriz mas 
        contendo apenas as informações dos funcionários pertencentes ao setor dado e
        não contém a informação do setor pois ele já foi dado.
    '''
    l = []
    for i in range(len(A)):
        if A[i][2] == s:
            l += [A[i].remove(s)]
    return l