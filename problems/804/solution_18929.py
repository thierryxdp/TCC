def filtra_pares(a):
    '''Função que recebe uma tupla com 4 elemetos inteiros como
    parametro e retorna uma nova tupla contendo apenas os elementos
    pares da tupla original, na ordem dada
    '''
    
    pares= tuple()
    if a[0]%2==0:
        tupla = (a[0],)
    if a[1]%2==0:
        tupla = (a[1],)
    if a[2]%2==0:
        tupla = (a[2],)
    if a[3]%2==0:
        tupla = (a[3],)
   
    return pares