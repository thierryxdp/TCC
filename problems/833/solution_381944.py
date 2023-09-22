def conta_numero(n,m):
    """A função calcula e retorna o número de vezes que um número (n) aparece na matriz(m);
    int,list[list,...]->int"""
    quantidade=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if  n in m[i][j]:
                quantidade=quantidade+1
    return quantidade