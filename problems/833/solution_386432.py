def conta_numero(numero,matriz):
    '''Retorna quantas vezes um inteiro aparece em uma matriz
    int, list(list,list,...) --> int'''
    
    qts_vezes = 0
    for linha in matriz:
        for Aij in linha:
            if Aij == numero:
                qts_vezes+=1
    return qts_vezes