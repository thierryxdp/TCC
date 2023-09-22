def conta_numero(numero,matriz):
    '''...'''
    
    R=[]
    n_linha=len(matriz)
    n_coluna=len(matriz[0])
    cont=0
    for i in range(n_linha):
        linha = n_coluna*[0]
        list.append(R,linha) 
        
    for elemento in matriz:
        if elemento == numero:
            cont+=1
    return cont