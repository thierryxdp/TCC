def filtra_pares(x,x,x,x):
    '''função que recebe uma tupla de 4 elementos int como parâmetro e retorna uma nova tupla contendo apenas os pares. (ent -> tuple, saida -> tuple'''
    tuple1 = (x,x,x,x)
    tuple2 = ()
    for valor in tuple1:
    if valor % 2 == 0:
        tuple2.append(valor)
    
    return tuple2