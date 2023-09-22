def conta_numero(numero,matriz):
    '''
    Conta quantas vezes um numero aparece em uma matriz
    int,list->int
    '''
    n=0
    for i in matriz:
        for j in matriz[i]:            
        	if j == numero:
                n=n+1
    return n