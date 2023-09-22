def filtra_pares():  #inserir a tupla
    '''assume que recebe uma tupla com 4 elementos e, a partir
 deles serão filtrados e retornados apenas os pares
 tupla -> tupla'''
    tupla_vazia = () #modelo a ser analisado
    
    if t[0] % 2 == 0:
    tupla_vazia = tupla_vazia + (t[0],)
    
    if t[1] % 2 == 0:
    tupla_vazia = tupla_vazia + (t[1],)
    
    if t[2] % 2 == 0:
    tupla_vazia = tupla_vazia + (t[2],)
    
    if t[3] % 2 == 0:
    tupla_vazia = tupla_vazia + (t[3],)
    
    return tupla_vazia()