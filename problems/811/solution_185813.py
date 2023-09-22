def colchao(medidas, H, L):
    medidas == []
    
    A = medidas[0]
    
    B = medidas[1]
    """ largura do colchao """
    
    C = medidas[2]
    """ altura do colchao """
   
    altura_porta = H
    largura_porta = L
    
    if H < B or H < C:
        return False
    elif L < B or L < C:
        return False
    else:
        return True