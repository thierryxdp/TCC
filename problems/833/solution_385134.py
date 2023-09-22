def conta_numero(numero,matriz):
    '''...'''
    
    R=[]
    n_linha=len(matriz)
    n_coluna=len(matriz[0])
    
    for i in range(n_linha):
        linha = n_coluna*[0]
        list.append(R,linha) 
        
    for i in range(n_linha):
        r=[]
        for j in range(n_coluna):
            list.append(r,list.count(matriz[i][j],numero))
            
    return r
    return matriz