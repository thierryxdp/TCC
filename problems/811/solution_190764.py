def colchao(medidas, H, L):
    '''Recebe as medidas medidas do colchao(altura, 
    largura e comprimento) e da porta (altura, largura),
    retorna True se o colchao passa pela porta;
    list, floar, float -> boolean'''
    
    if (medidas[0] <= H and medidas[1] <= L) or (medidas[0] <= L and medidas[2] <= H) or (medidas[0] <= L and medidas[1] <=H):
        return True
    else:
        return False