def filtra_pares(tupla_in):
    '''Recebe uma tupla com quatro inteiros e retorna uma
    tupla com apenas os elementos pares, na ordem 
    original
    tuple -> tuple'''
    tupla_out = ()
    if tupla_in[0] % 2 == 0 and tupla_in[0] != 1:
        tupla_out = tupla_out + (tupla_in[0],)
    if tupla_in[1] % 2 == 0 and tupla_in[1] != 1:
        tupla_out = tupla_out + (tupla_in[1],)
    if tupla_in[2] % 2 == 0 and tupla_in[2] != 1:
        tupla_out = tupla_out + (tupla_in[2],)
    if tupla_in[3] % 2 == 0 and tupla_in[3] != 1:
        tupla_out = tupla_out + (tupla_in[3],)
    
    return tupla_out