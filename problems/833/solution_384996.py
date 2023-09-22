def conta_numero(numero,matriz):
    '''...'''
    
    R=[]
    cont=0
    n_linha=len(matriz)
    n_coluna=len(matriz[0]) 
    
    for i in range(n_linha):
        linha = n_coluna*[0]
        list.append(R,linha) 
        
    for i in range(n_linha):
        for j in range(n_coluna):
            pos = list.count(matriz,numero)
            pos+=1
                    
    return pos