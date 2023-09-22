def colchao(medidas, H, L):
    medidas == []
    
    A = medidas[0]
    
    B = medidas[1]
    """ largura do colchao """
    
    C = medidas[2]
    """ comprimento do colchao do colchao """
   
    altura_porta = H
    largura_porta = L
    
    if (H and L) < (B or C):
        return True
    else:
        return False