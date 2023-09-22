def filtra_pares(tupla):
    '''Retorna uma tupla contendo apenas os elementos pares da tupla original;
    tupla-> tupla.'''
    tupla2=()
    if tupla[0]%2==0:
        tupla2=tupla2+tupla[0:1:]
    if tupla[1]%2==0:
         tupla2=tupla2+tupla[1:2:]
    if tupla[2]%2==0:
        tupla2=tupla2+tupla[2:3:]
    if tupla[3]%2==0:
        tupla2=tupla2+tupla[3::]
    return tupla2
    else:
        return ()