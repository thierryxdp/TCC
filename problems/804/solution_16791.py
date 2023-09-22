filtra_pares(a,b,c,d):
    '''Função que recebe uma tupla com 4 numeros inteiros
    e retorna na mesma ordem uma tupla com somente os 
    numeros pares da tupla recebida
    tuple->tuple'''
    par = ()
    if a % 2== 0:
        par = par + (a,)
    if b % 2== 0:
        par = par + (b,)
    if c % 2== 0:
        par = par + (c,)
    if d % 2== 0:
        par =  + (d,)
    return par