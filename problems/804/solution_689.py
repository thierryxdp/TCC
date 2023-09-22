def filtra_pares(elementos):
    '''função que verifica e retorna, a partir de uma tupla com 4 elementos inteiros, uma outra tupla com os elementos pares da anterior; tuple -> tuple'''
    
    resto1 = elementos[0]%2
    resto2 = elementos[1]%2
    resto3 = elementos[2]%2
    resto4 = elementos[3]%2
    
    if resto1==0 and resto2==0 and resto3==0 and resto4==0:
        return tuple(elementos)
    
    elif resto1==0 and resto2==0 and not resto3==0 and not resto4==0:
        return (elementos[0], elementos[1])
    
    elif resto1==0 and resto2==0 and resto3==0 and not resto4==0:
        return (elementos[0], elementos[1], elementos[2])
    
    elif resto1==0 and not resto2==0 and resto3==0 and not resto4==0:
        return (elementos[0], elementos[2])
    
    elif not(resto1==0 and resto2==0 and resto3==0) and resto4==0:
        return ((elementos[3],))