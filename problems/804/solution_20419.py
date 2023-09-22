def filtra_pares(numeros):
    '''Recebe uma tupla com 4 elementos inteiros como parâmetro, e retorna uma nova tupla com apenas os números pares da tupla original
    tuple->tuple'''
    pares=()
    if numeros[0]%2==0:
        pares=(numeros[0],)
    if numeros[1]%2==0:
        pares=pares+(numeros[1],)
    if numeros[2]%2==0:
        pares=pares+(numeros[2],)
    if numeros[3]%2==0:
        pares=pares+(numeros[3],)
    return pares