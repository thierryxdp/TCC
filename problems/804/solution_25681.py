def filtra_pares(tupla):
    '''Função que, dada uma tupla composta por 4 elementos
    tuple(int,int,int,int)-> tuple'''
    filtrados= ()
    if tupla[0]%2==0:
        filtrados= filtrados+ (tupla[0],)
    if tupla[1]%2==0:
        filtrados= filtrados+ (tupla[1],)
    if tupla[2]%2==0:
            filtrados= filtrados+ (tupla[2],)
    if tupla[3]%2==0:
                    filtrados= filtrados+ (tupla[3],)
                    return filtrados