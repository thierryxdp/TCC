def conta_numero(numero,matriz):
    '''teste'''
    
    
    quantidade=0
    
    
    for i in range(len(matriz)):
        for j in matriz[i]:
            if j==numero:
                quantidade=quantidade+1
        
    return quantidade