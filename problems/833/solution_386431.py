def conta_numero(n,m):
    '''Função que dado um número inteiro(n) e uma matriz(m), retorna a 
    quantidade de vezes que esse número aparece na matriz.
    int,list->int'''
    p=0
    quantidade=0
    for elemento in m:
        quantidade=quantidade + list.count(m[p],n)
        p= p+1
    return quantidade