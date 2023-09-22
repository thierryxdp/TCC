def filtra_pares(tupla):
    '''Função que recebe uma tupla com 4 numeros inteiros
    e retorna na mesma ordem uma tupla com somente os 
    numeros pares da tupla recebida
    tuple->tuple'''
    par = ()
    if tupla[0] % 2== 0:
        par = par + (tupla[0],)
    if tupla[1] % 2== 0:
        par = par + (tupla[1],)
    if tupla[2] % 2== 0:
        par = par + (tupla[2],)
    if tupla[3] % 2== 0:
        par = par + (tupla[3],)
    return par