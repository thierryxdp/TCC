h_colchao = medidas[0]
    l_colchao = medidas[1]
    c_colchao = medidas[2]
    
    #altura e largura
    if(h_colchao <= H and l_colchao <= L):
        return True
    elif(h_colchao <= L and l_colchao <= H):
        return True
    
    #altura e comprimento
    elif(h_colchao <= H and c_colchao <= L):
        return True
    
    elif(h_colchao <= L and c_colchao <= H):
        return True
    
    #largura e comprimento
    elif(l_colchao <= H and c_colchao<= L):
        return True
    elif(l_colchao <= L and c_colchao<=H):
        return True
    else:
        return False