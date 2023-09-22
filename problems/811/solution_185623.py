def colchao(medidas,H,L):
    """funcao que calcua as medidas do colchao"""
    medidas.sort()
    altura=medidas[0]
    largura=medidas[1]
    comprimento=medidas[2]
    if comprimento<H:
        return True 
    if largura<H:
        return True
    if largura<L:
        return True
    
    return False