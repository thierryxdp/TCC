def filtra_pares(tupla):
    '''Recebe uma tupla com números inteiros e retorna uma 
   tupla apenas com seus elementos pares
   		tupla -> tupla'''
    tupla_final = ()
    for i in tupla:
        if i % 2 == 0:
            tupla_final = tupla_final + (i,)
    return tupla_final