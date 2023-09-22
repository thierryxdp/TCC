def filtra_pares(tupla):
    '''Função que filtra os números pares de uma tupla contendo
    4 elementos inteiros
    tuple->tuple'''
    
    novatupla = ()
    
    if tupla[0]%2==0:
        novatupla = novatupla + (tupla[0],)
    if tupla[1]%2==0:
        novatupla = novatupla + (tupla[1],)
    if tupla[2]%2==0:
        novatupla = novatupla + (tupla[2],)
    if tupla[3]%2==0:
        novatupla = novatupla + (tupla[3],)
    return novatupla