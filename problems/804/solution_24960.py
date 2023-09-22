def par(num):
    '''função que retorna true caso o número dado seja par
    e false caso seja ímpar ou zero;
    int/float->bool'''
    return num%2==0
def filtra_pares(t):
    '''função que retorna uma tupla com
    os numeros pares dado uma tupla contendo 4 números inteiros;
    tup->tup'''
    pares=()
    if par(t[0],):
        pares=pares+(t[0],)
    if par(t[1],):
        pares=pares+(t[1],)
    if par(t[2],):
        pares=pares+(t[2],)
    if par(t[3],):
        pares=pares+(t[3],)
    return pares