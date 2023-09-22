def colchao(medidas, H, L):
    """ Dado a Entrada sendo as medidas de um colchão no formato lista
    [A,B,C], mais as medidas de uma porta H(altura) e L(Largura), retorna
    se é possível desse colchao passar po essa porta. """
    
    medidas == []
    
    A = medidas[0]
    
    B = medidas[1]
    """ largura do colchao """
    
    C = medidas[2]
    """ comprimento do colchao do colchao """
   
    altura_porta = H
    largura_porta = L
    
    if H > (B or C):
        return True
    if L > (B or C):
        return True
    else:
        return False