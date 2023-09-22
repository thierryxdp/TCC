def conta_numero(numero,matriz):
    '''
    int,list->int
    '''
    con=0
    for n in range(len(matriz)):
        
        m=matriz[n]
        for k in range(len(m)):
            if m[k]==numero:
                con=con+1
            else:
                con
    return con