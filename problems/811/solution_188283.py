def colchao(medidas, H, L):
    """A função ve se a medida do colchão é suficiente para passar pela porta com as medidas da porta sendo H(altura) e L (Largura)
    Entrada- int Saida- booleano"""
    if(medidas[1] <= H) or (medidas[2] <= H):
        return True
    elif(medidas[1] <= L) or (medidas[2] <= L):
        return True
    else:
        return False