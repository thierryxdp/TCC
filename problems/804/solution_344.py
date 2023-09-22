def filtra_pares(tupla4):
    '''Recebe uma tupla com 4 elementos inteiros (tupla4) e retorna uma nova
    tupla contendo apenas os elementos pares da tupla original, na mesma ordem
    em que se encontravam.
    tuple -> tuple
    
    Explicação: verifica um por um os elementos da tupla de entrada para descobrir 
    se são pares ou não, depois cria uma nova tupla onde apenas os números pares
    da tupla original aparecem (na mesma ordem em que se encontravam) '''

    if tupla4[0]%2 ==0:
        x = (tupla4[0],)
    else:
        x = ()
    if tupla4[1]%2 ==0:
        x1 = (tupla4[1],)
    else:
        x1 = ()
    if tupla4[2]%2 ==0:
        x2 = (tupla4[2],)
    else:
        x2 = ()
    if tupla4[3]%2 ==0:
        x3 = (tupla4[3],)
    else:
        x3 = ()

    return x + x1 + x2 + x3