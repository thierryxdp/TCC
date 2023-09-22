def busca(s,A):
    '''
    	A função recebe uma string (nome de um setor de uma empresa) e uma matriz
        com as informações dos funcionários dessa empresa (cada linha da matriz 
        contém as seguintes informações de um funcionário: nome, registro, setor e
        número; respectivamente). Com isso, a função vai checar quais funcionários
        pertencem ao setor informado e retornará uma matriz com as informações 
        desses funcionários, mas sem o setor já que isso já é sabido.
        s -> string (setor da empresa)
        A -> list (matriz em que cada linha contém informações de um funcionários 
        da empresa, além disso, as informações são strings)
    '''
    l = []
    for i in range(len(A)):
        if s in A[i]:
            A[i].remove(s)
            l += [A[i]]
	return l