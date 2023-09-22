def filtra_pares(tupla):
    '''Retorna uma tupla contendo apenas os elementos pares da tupla original;
    tupla-> tupla.'''
    z=tuple(tupla)
    tupla2=()
    if z[0]%2==0:
        tupla2=tupla2+z[0:1:]
    if z[1]%2==0:
         tupla2=tupla2+z[1:2:]
    if z[2]%2==0:
        tupla2=tupla2+z[2:3:]
    if z[3]%2==0:
        tupla2=tupla2+z[3::]
    return tupla2