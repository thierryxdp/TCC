def filtra_pares(tupla):
    ''' 
    Função recebe uma tupla contendo quatro elementos inteiros. 
    Retorna uma tupla contendo os elementos pares
    '''
    tupla_par = 0 
    for par in tupla:
        if par % 2 == 0:
            tupla_par.append(par)
        elif par % 2 != 0:
            continue
    
    return (tupla_par)