def colchao(medidas,H,L):
    H_colchao = medidas[0]
    L_colchao = medidas[1]
    C_colchao = medidas[2]
    
    #Altura e Largura
    if(H_colchao <= H and L_colchao <= L):
        return True
    elif(H_colchao <= L and L_colchao <= H):
        return True
    
    #altura e comprimento
    elif(H_colchao <= H and C_colchao <= L):
        return True
    
    elif(H_colchao <= L and C_colchao <= H):
        return True
    
    #largura e comprimento
    elif(L_colchao <= H and C_colchao<= L):
        return True
    elif(L_colchao <= L and C_colchao<= H):
        return True
    else:
        return False